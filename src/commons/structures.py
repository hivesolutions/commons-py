#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class BudyApp(appier.WebApp):

    def __init__(self):
        appier.WebApp.__init__(
            self,
            name = "budy",
            parts = (
                appier_extras.AdminPart,
            )
        )

if __name__ == "__main__":
    app = BudyApp()
    app.serve()
