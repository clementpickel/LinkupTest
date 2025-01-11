from env import LINKUP_APIKEY
from linkup import LinkupClient

class LinkupInstance:
    client = LinkupClient(api_key=LINKUP_APIKEY)

    def search(self, query: str, depth: str = "standard", output_type: str = "searchResults") -> dict:
        return self.client.search(
            query=query,
            depth=depth, # standard or deep
            output_type=output_type # searchResults or sourcedAnswer or structuredOutput
        )