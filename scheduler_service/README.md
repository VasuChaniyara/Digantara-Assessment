## 1. Create a virtual environment:
      python -m venv assignmentenv
      source assignmentenv/Scripts/activate

## 2. Install dependencies:
    pip install -r requirements.txt

## 3. Run the FastAPI application:
    uvicorn main:app --reload

## 4. API Endpoints:
    GET /jobs: List all jobs
    GET /jobs/{id}: Retrieve job details by ID
    POST /jobs: Create a new job
    DELETE /jobs/{id}: Delete a job by ID

   ### 4.1 GET, POST and DELETE jobs using Postman:
        1. Send a GET Request
                Set Request Type:
                    Ensure the request type is set to GET
                Enter URL:
                    Enter http://127.0.0.1:8000/jobs in the URL field
                Send Request:
                    Click the Send button
                    The response from the server will be displayed in the lower section of the window
        2. Send a POST Request
                Set Request Type:
                    Change the request type to POST
                Enter URL:
                    Enter http://127.0.0.1:8000/jobs in the URL field
                Set Headers:
                    Click on the Headers tab
                    Add a new header with 'Key' set to 'Content-Type' and 'Value' set to 'application/json'
                Set Body:
                    Click on the Body tab
                    Select raw and ensure the format is set to JSON from the dropdown menu
                    Enter the JSON data:
                        {
                        "name": "Sample Job",
                        "interval": "daily",
                        "details": "Dummy job for testing"
                        }
                Send Request:
                    Click the Send button
                    The response from the server will be displayed in the lower section of the window
        3. Send a DELETE Request
                Set Request Type:
                    Change the request type to DELETE
                Enter URL:
                    Enter http://127.0.0.1:8000/jobs/{job_id} in the URL field, replacing {job_id} with the ID of the job you want to delete (e.g., http://127.0.0.1:8000/jobs/1)
                Send Request:
                    Click the Send button
                    The response from the server will be displayed in the lower section of the window.
        
## 5. View API Documentation:
      1. Swagger UI: 
            Open a web browser and go to http://127.0.0.1:8000/docs to access the interactive API documentation provided by FastAPI's Swagger UI.
      2. ReDoc: 
            Open a web browser and go to http://127.0.0.1:8000/redoc for an alternative view of the API documentation.
