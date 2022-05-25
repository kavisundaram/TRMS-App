from controllers import emp_controller, home_controller, reimb_controller


def route(app):
    home_controller.route(app)
    emp_controller.route(app)
    reimb_controller.route(app)

