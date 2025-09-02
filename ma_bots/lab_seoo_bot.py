from typing import Optional
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


def event_Lab_seoo(category_r: str, category3: str) -> Optional[str]:
    """
    Retrieve category lab information based on the provided category using a chain of handlers.
    """
    request = TranslationRequest(category_r, category3)

    # Create the chain of handlers
    handler_chain = NewP17FinallHandler(
        AmbassadorsTabHandler(
            TeamWorkClubHandler(
                Event2Handler(
                    PopAll2018Handler(
                        CentriesYearsDecHandler(
                            Test4_2018_JobsHandler(
                                JobsInMultiSportsHandler(
                                    UniverHandler(
                                        TestFilmsHandler(
                                            NatsHandler(
                                                YeTsBotHandler(
                                                    WorkUSStateHandler(
                                                        WorkPeoplesHandler(Test3Handler(WikidataHandler()))
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )

    return handler_chain.handle(request)
