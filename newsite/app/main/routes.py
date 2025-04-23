from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import User, Group, Notification, Module
from app import db
from app.main import bp

@bp.route('/')
def index():
    return render_template('main/index.html')

@bp.route('/profile')
@login_required
def profile():
    return render_template('main/profile.html')

@bp.route('/group-management')
@login_required
def group_management():
    if not (current_user.is_group_admin or current_user.is_admin):
        flash('You do not have permission to access this page.', 'error')
        return redirect(url_for('main.index'))
        
    if current_user.is_admin:
        groups = Group.query.all()
    else:
        groups = Group.query.filter_by(admin_id=current_user.id).all()
        
    # Get all modules for progress display
    modules = Module.query.order_by(Module.order).all()
        
    return render_template('main/group_management.html', groups=groups, modules=modules)

@bp.route('/group/create', methods=['POST'])
@login_required
def create_group():
    if not current_user.is_group_admin:
        flash('You do not have permission to create groups.', 'error')
        return redirect(url_for('main.index'))
        
    name = request.form.get('name')
    description = request.form.get('description')
    
    if not name:
        flash('Group name is required.', 'error')
        return redirect(url_for('main.group_management'))
        
    if Group.query.filter_by(name=name).first():
        flash('A group with this name already exists.', 'error')
        return redirect(url_for('main.group_management'))
        
    group = Group(
        name=name,
        description=description,
        admin_id=current_user.id
    )
    db.session.add(group)
    db.session.commit()
    
    flash('Group created successfully.', 'success')
    return redirect(url_for('main.group_management'))

@bp.route('/group/<int:group_id>/invite', methods=['POST'])
@login_required
def invite_to_group(group_id):
    group = Group.query.get_or_404(group_id)
    
    if not (current_user.is_admin or group.admin_id == current_user.id):
        flash('You do not have permission to invite users to this group.', 'error')
        return redirect(url_for('main.group_management'))
        
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    
    if not user:
        flash(f'No user found with email: {email}', 'error')
        return redirect(url_for('main.group_management'))
        
    if user in group.members:
        flash('User is already a member of this group.', 'error')
        return redirect(url_for('main.group_management'))
        
    # Check for existing invitation
    existing_notification = Notification.query.filter(
        Notification.user_id == user.id,
        Notification.type == 'group_invite'
    ).first()
    
    # Only check data field if notification exists
    if existing_notification and existing_notification.data and 'group_id' in existing_notification.data:
        if int(existing_notification.data['group_id']) == group_id:
            flash('User already has a pending invitation.', 'error')
            return redirect(url_for('main.group_management'))
        
    # Create invitation notification
    notification = Notification(
        user_id=user.id,
        type='group_invite',
        content=f'You have been invited to join {group.name} by {current_user.username}',
        data={'group_id': group_id}
    )
    db.session.add(notification)
    db.session.commit()
    
    flash(f'Invitation sent successfully to {email}.', 'success')
    return redirect(url_for('main.group_management'))

@bp.route('/group/<int:group_id>/remove-member/<int:user_id>')
@login_required
def remove_group_member(group_id, user_id):
    group = Group.query.get_or_404(group_id)
    user = User.query.get_or_404(user_id)
    
    if not (current_user.is_admin or group.admin_id == current_user.id):
        flash('You do not have permission to remove members from this group.', 'error')
        return redirect(url_for('main.group_management'))
        
    if user.group_id != group_id:
        flash('User is not a member of this group.', 'error')
        return redirect(url_for('main.group_management'))
        
    user.group = None
    db.session.commit()
    
    flash('Member removed successfully.', 'success')
    return redirect(url_for('main.group_management')) 