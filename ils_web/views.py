import os
import shutil

from django.views.generic import FormView, TemplateView

from ils_web.forms import DataForm
from ils_web.settings import BASE_DIR
from maths.async_simulator_wrapper import AsyncSimulatorWrapper
from maths.simulator import Simulator


class DataInsertFormView(FormView):
    form_class = DataForm
    template_name = "data_insert.html"
    success_url = "/show"

    def form_valid(self, form):
        s = Simulator(
            step=form.cleaned_data["tick_time"],
            iterations=form.cleaned_data["total_ticks"],
            start_point=int(form.cleaned_data["start_point"]),
            end_point=int(form.cleaned_data["end_point"]),
            save_palace=BASE_DIR + "/plots/"
        )
        s.set_gravity_expression(form.cleaned_data["gravity_expression"])
        s.set_friction_expression(form.cleaned_data["friction_expression"])
        s.set_plane_expression(form.cleaned_data["plane_expression"])

        shutil.rmtree(BASE_DIR + "/plots", ignore_errors=True)
        os.mkdir(BASE_DIR + "/plots")

        a_s = AsyncSimulatorWrapper(s)
        a_s.start()

        return super().form_valid(form)


class ShowView(TemplateView):

    def setup(self, request, *args, **kwargs):
        super().setup(request, args, kwargs)
        self.template_name = "show.html" if os.path.isfile(BASE_DIR + "/plots/plot.mp4") else "showWIP.html"
