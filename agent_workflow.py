class AgentWorkflow:

    def plan(self, query):
        return ['Retrieve Data', 'Analyze', 'Generate Answer']

    def execute(self, query):
        return {
            'steps': self.plan(query),
            'status': 'Completed'
        }
