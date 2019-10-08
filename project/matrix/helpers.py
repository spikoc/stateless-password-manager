"""
    Contains methods that have the business logic to process the requests.
"""
from project.matrix.forms import EditForm
from project.matrix.models import Algorithm


def prepare_form_data(model):
    """
        Initialize a new form - if the model is not empty, get the form data of the fields from it,
    otherwise use default values.

    :param model: A :class:`project.matrix.models.Matrix` object.
    :return     : A :class:`project.matrix.forms.EditForm` object.
    """
    form = EditForm(obj=model)

    # .................................specify the available options in the selection field
    form.algorithm.choices = [(0, '-- select a hash algorithm --')]
    form.algorithm.choices.extend(
        [(x.id, x.name) for x in Algorithm.query.order_by(Algorithm.name).all()])

    # .................................set the default option in the selection field
    form.algorithm.process_data(model.algorithm_id)

    return form
