import nipype


def build_nuisance_workflow(workflow_config):
    """
    Build a workflow for nuisance variable regression
    :param workflow_config: dictionary containing workflow parameters
    :return: 
    """

    return_value = False
    if "nuisance" in workflow_config:
        return_value = True

    return return_value
