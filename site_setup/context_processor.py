from site_setup.models import SiteSetup

def context_processor_example(request):
    return {
        'example':'context'
    }


def site_setup(request):
    data = SiteSetup.objects.order_by('-id').first()
    return {
        'site_setup': data
}