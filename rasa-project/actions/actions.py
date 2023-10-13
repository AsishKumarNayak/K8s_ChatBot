from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from kubernetes import client, config
class ActionHelloWorld(Action):

class ActionCheckPodStatus(Action):
    def name(self) -> Text:
        return "action_check_pod_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Load Kubernetes configuration from a file or a service account in the cluster
            config.load_kube_config()  # You can also use load_incluster_config() for in-cluster configurations

            # Define the namespace and pod name you want to check the status of
            namespace = "default"  # Change this to your desired namespace
            pod_name = "your_pod_name_here"  # Change this to the specific pod name you want to check

            # Create a Kubernetes API client
            api_instance = client.CoreV1Api()
            print("api_instance: ", api_instance)

            # Retrieve pod information
            pod_info = api_instance.read_namespaced_pod(name=pod_name, namespace=namespace)

            # Extract the pod status
            pod_status = pod_info.status.phase

            # Construct a response message
            response = f"The pod {pod_name} is in {pod_status} phase."

            # Send the response to the user
            dispatcher.utter_message(text=response)

        except Exception as e:
            # Handle any exceptions or errors that may occur during the Kubernetes interaction
            dispatcher.utter_message("An error occurred while checking the pod status.")

        return []
