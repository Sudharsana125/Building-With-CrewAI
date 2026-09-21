from crewai.flow.flow import Flow, start


class JobApplicationFlow(Flow):

    @start()
    def receive_application(self):
        print("Application received!")
        return "Application received successfully."


flow = JobApplicationFlow()

result = flow.kickoff()

print("\n--- RESULT ---")
print(result)