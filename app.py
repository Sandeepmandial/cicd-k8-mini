from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Dashboard</title>

        <!-- Bootstrap -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

        <style>
            body {{
                background: linear-gradient(135deg, #1f4037, #99f2c8);
                min-height: 100vh;
                color: white;
            }}

            .card {{
                border-radius: 20px;
                backdrop-filter: blur(10px);
                background: rgba(255,255,255,0.1);
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }}

            .btn-custom {{
                border-radius: 30px;
                padding: 10px 20px;
                transition: 0.3s;
            }}

            .btn-custom:hover {{
                transform: scale(1.1);
            }}
        </style>
    </head>

    <body>

    <!-- NAVBAR -->
    <nav class="navbar navbar-dark bg-dark px-4">
        <span class="navbar-brand">🚀 CI/CD Dashboard</span>
        <button class="btn btn-success btn-custom" onclick="location.reload()">🔄 Refresh</button>
    </nav>

    <div class="container mt-5">

        <div class="row">

            <!-- MAIN CARD -->
            <div class="col-md-8">
                <div class="card p-4 text-center">
                    <h2>Pipeline Status</h2>
                    <h4 class="mt-3 text-success">✅ SUCCESS</h4>

                    <p class="mt-3">Last Updated:</p>
                    <h5>{now}</h5>

                    <button class="btn btn-primary btn-custom mt-3" onclick="alert('Pipeline is running successfully!')">
                        Check Status
                    </button>
                </div>
            </div>

            <!-- SIDE PANEL -->
            <div class="col-md-4">
                <div class="card p-4">
                    <h4>Project Info</h4>
                    <p>🔹 App: Flask CI/CD</p>
                    <p>🔹 Tools: Jenkins, Docker, Kubernetes</p>
                    <p>🔹 Environment: Local Cluster</p>
                </div>

                <div class="card p-4 mt-3 text-center">
                    <h5>Quick Actions</h5>

                    <button class="btn btn-warning btn-custom mt-2 w-100"
                        onclick="window.open('/about')">
                        📄 About Project
                    </button>

                    <button class="btn btn-danger btn-custom mt-2 w-100"
                        onclick="alert('Simulated Deployment Restart')">
                        🔁 Restart Deployment
                    </button>
                </div>
            </div>

        </div>

    </div>

    </body>
    </html>
    """

@app.route('/about')
def about():
    return """
    <h1>About This Project</h1>
    <p>This is a CI/CD pipeline using Jenkins, Docker, and Kubernetes.</p>
    <a href="/">Go Back</a>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)