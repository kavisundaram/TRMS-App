def route(app):
    @app.route("/")
    def hello():
        return "Tuition Reimbursement System"