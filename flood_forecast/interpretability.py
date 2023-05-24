from captum.attr import IntegratedGradients, DeepLift, GradientShap, NoiseTunnel, FeatureAblation
from typing import Tuple, Dict

attr_dict = {"IntegratedGradients": IntegratedGradients, "DeepLift": DeepLift, "GradientSHAP": GradientShap,
             "NoiseTunnel": NoiseTunnel, "FeatureAblation": FeatureAblation}


def run_attribution(model, test_loader, method, additional_params: Dict) -> Tuple:
    """Function that creates attribution for a model based on Captum.

    :param model: The deep learning model to be used for attribution. This should be a PyTorch model.
    :type model: _type_
    :param test_loader: _description_
    :type test_loader: _type_
    :param method: _description_
    :type method: _type_
    :return: d
    :rtype: Tuple
    """

    attribution_method = attr_dict[method](model)
    x, y = test_loader[0]
    attributions, approximation_error = attribution_method.attribute(x.unsqueeze(0), **additional_params)
    return attributions, approximation_error
