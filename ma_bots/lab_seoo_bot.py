from .translation_handlers import (
    TranslationRequest,
    NewP17FinallHandler,
    AmbassadorsTabHandler,
    TeamWorkClubHandler,
    Event2Handler,
    PopAll2018Handler,
    CentriesYearsDecHandler,
    Test4_2018_JobsHandler,
    JobsInMultiSportsHandler,
    UniverHandler,
    TestFilmsHandler,
    NatsHandler,
    YeTsBotHandler,
    WorkUSStateHandler,
    WorkPeoplesHandler,
    Test3Handler,
    WikidataHandler,
)

def event_Lab_seoo(category_r, category3):
    """
    Retrieve category lab information based on the provided category using a chain of handlers.
    """
    request = TranslationRequest(category_r, category3)

    # Create the chain of handlers
    handler_chain = NewP17FinallHandler()
    handler_chain._successor = AmbassadorsTabHandler()
    handler_chain._successor._successor = TeamWorkClubHandler()
    handler_chain._successor._successor._successor = Event2Handler()
    handler_chain._successor._successor._successor._successor = PopAll2018Handler()
    handler_chain._successor._successor._successor._successor._successor = CentriesYearsDecHandler()
    handler_chain._successor._successor._successor._successor._successor._successor = Test4_2018_JobsHandler()
    handler_chain._successor._successor._successor._successor._successor._successor._successor = JobsInMultiSportsHandler()
    handler_chain._successor._successor._successor._successor._successor._successor._successor._successor = UniverHandler()
    handler_chain._successor._successor._successor._successor._successor._successor._successor._successor._successor = TestFilmsHandler()
    handler_chain._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor = NatsHandler()
    handler_chain._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor = YeTsBotHandler()
    handler_chain._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor = WorkUSStateHandler()
    handler_chain._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor = WorkPeoplesHandler()
    handler_chain._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor = Test3Handler()
    handler_chain._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor._successor = WikidataHandler()

    return handler_chain.handle(request)
