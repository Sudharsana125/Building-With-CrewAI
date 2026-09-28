from crewai.flow.flow import Flow, start, listen


class JobApplicationFlow(Flow):

    @start()
    def receive_application(self):
        print("Application received!")
        return "Application received successfully."

    @listen(receive_application)
    def check_application(self):
        print("Checking application...")
        return "Application checked."


flow = JobApplicationFlow()

result = flow.kickoff()

print("\n--- RESULT ---")
print(result)
