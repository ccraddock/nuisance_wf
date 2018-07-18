from unittest import TestCase

import nuisance_wf


class TestNuisanceWorkflow(TestCase):

    def test_workflow_build(self):
        nuisance_parameters = {"nuisance": True}
        self.assertTrue(nuisance_wf.build_nuisance_workflow(nuisance_parameters))

    def test_workflow_build_anti(self):
        nuisance_parameters = {"filtering": True}
        self.assertFalse(nuisance_wf.build_nuisance_workflow(nuisance_parameters))
