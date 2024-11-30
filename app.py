from flask import Flask, request, jsonify
from src.Service_Layer.Interaction_Manager import Interaction_Manager
from mongoDB.CRUD_api import Database_Manager
from src.Service_Layer.User import User



app = Flask(__name__)


interaction_manager = Interaction_Manager()


@app.route('/add_washer', methods=['POST'])
def add_washer():
    try:
        success = interaction_manager.add_washer()
        return jsonify({'success': success, 'message': 'Washer added successfully' if success else 'Failed to add washer'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/add_dryer', methods=['POST'])
def add_dryer():
    try:
        success = interaction_manager.add_dryer()
        return jsonify({'success': success, 'message': 'Dryer added successfully' if success else 'Failed to add dryer'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
    
@app.route('/get_machines', methods=['GET'])
def get_machines():
    return jsonify({'DB_machines': [machine.__dict__ for machine in Database_Manager().get_all_machines()]})

@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.json
    sending_user_name = data.get('sending_user_name')
    receiving_user_name = data.get('receiving_user_name')
    sending_user = Database_Manager().get_specific_user(sending_user_name)
    receiving_user = Database_Manager().get_specific_user(receiving_user_name)
    message = data.get('message')
    
    try:
        interaction_manager.send_notification(sending_user, receiving_user, message)
        return jsonify({'success': True, 'message': 'Notification sent successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    # print(f"Received data: {data}")  Debugging: check what data is coming in

    user_name = data.get('user_name')
    notification_preference = data.get('notification_preference')
    user_phone_number = int(data.get('user_phone_number'))
    user_email = data.get('user_email')
    phone_carrier = data.get('phone_carrier')
    is_admin = data.get('is_admin', False)  # Default to False if is_admin is not provided
    is_admin = True if is_admin == True else False
    password = data.get('password', 'defaultpassword123')
    password = 'defaultpassword123' if password == None else password

    if not user_name:
        return jsonify({'success': False, 'error': 'No username was provided'}), 400

    try:
        success = interaction_manager.add_user(user_name, notification_preference, user_phone_number, user_email, phone_carrier, is_admin, password)
        return jsonify({'success': success, 'message': 'User added successfully' if success else 'Failed to add user'})
    except Exception as e:
        print(f"Error adding user: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/remove_user', methods=['DELETE'])
def remove_user():
    data = request.json
    user_name = data.get('user_name')
    
    try:
        success = interaction_manager.remove_user(user_name)
        return jsonify({'success': success, 'message': 'User removed successfully' if success else 'Failed to remove user'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/authenticate_log_in', methods=['POST'])
def authenticate_log_in():
    data = request.json
    email_address = data.get('email_address')
    password = data.get('password')
    
    try:
        success = interaction_manager.authenticate_log_in(email_address, password)
        return jsonify({'success': success, 'message': 'Authentication successful' if success else 'Authentication failed'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
 
@app.route('/create_session', methods=['POST'])
def create_session():
    data = request.json
    machine_id = data.get('machine_id')
    user_name = data.get('user_name')
    
    # Validate machine_id and user_name existence
    if machine_id not in [machine.machine_id for machine in Database_Manager().get_all_machines()] or user_name not in [user.user_name for user in Database_Manager().get_valid_users()]:
        return jsonify({'success': False, 'error': 'Machine or User not found'}), 404

    # Fetch the machine and user
    user = Database_Manager().get_specific_user(user_name)

    try:
        # Call instance method on interaction_manager
        success = interaction_manager.create_session(machine_id, user)
        return jsonify({'success': success, 'message': 'Session created successfully' if success else 'Failed to create session'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/end_session', methods=['POST'])
def end_session():
    data = request.json
    machine_id = data.get('machine_id')
    user_name = data.get('user_name')

    # Validate machine_id and user_name existence
    if machine_id not in [machine.machine_id for machine in Database_Manager().get_all_machines()] or user_name not in [user.user_name for user in Database_Manager().get_valid_users()]:
        return jsonify({'success': False, 'error': 'Machine or User not found'}), 404

    # Fetch the machine and user
    user = Database_Manager().get_specific_user(user_name)
    
    try:
        # Call instance method on interaction_manager
        success = interaction_manager.end_session(machine_id, user)
        return jsonify({'success': success, 'message': 'Session ended successfully' if success else 'Failed to end session'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/set_out_of_order', methods=['POST'])
def set_out_of_order():
    data = request.json
    machine_id = data.get('machine_id')
    user_name = data.get('user_name')

    # Validate machine_id and user_name existence
    if machine_id not in [machine.machine_id for machine in Database_Manager().get_all_machines()] or user_name not in [user.user_name for user in Database_Manager().get_valid_users()]:
        return jsonify({'success': False, 'error': 'Machine or User not found'}), 404

    # Fetch the machine and user
    user = Database_Manager().get_specific_user(user_name)

    try:
        # Call set_out_of_order method
        success = interaction_manager.set_out_of_order(machine_id, user)
        return jsonify({'success': success, 'message': 'Machine status updated successfully' if success else 'Failed to update machine status'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/get_status', methods=['GET'])
def get_status():
    machine_id = request.json.get('machine_id')
    
    if machine_id not in [machine.machine_id for machine in Database_Manager().get_all_machines()]:
        return jsonify({'success': False, 'error': 'User not found'}), 404
    
    try:
        # Call get_status method
        status = interaction_manager.get_status(machine_id)
        return jsonify({'success': True, 'status': status})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/notify_user', methods=['POST'])
def notify_user():
    data = request.json
    machine_id = data.get('machine_id')
    user_name = data.get('user_name')

    # Fetch the machine and user
    user = Database_Manager().get_specific_user(user_name)

    if not user:
        return jsonify({'success': False, 'error': 'User not found'}), 404
    
    try:
        # Call notify_user method
        success = interaction_manager.notify_user(machine_id, user)
        return jsonify({'success': success, 'message': 'Notification sent successfully' if success else 'Failed to send notification'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
