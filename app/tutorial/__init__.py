from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from .models import DBSession, Base

import os
import logging
import sqlite3

from pyramid.events import ApplicationCreated
from pyramid.events import NewRequest
from pyramid.events import subscriber


def main(global_config, **settings):

    # # @subscriber(ApplicationCreated)
    # def application_created_subscriber():
    #     log.warning('Initializing database...')
    #     with open(os.path.join(here, 'schema.sql')) as f:
    #         stmt = f.read()
    #         settings = event.app.registry.settings
    #         db = sqlite3.connect(settings['db'])
    #         db.executescript(stmt)
    #         db.commit()

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings,
                          root_factory='tutorial.models.Root')
    config.include('pyramid_chameleon')
    config.add_route('wiki_view', '/')
    config.add_route('main', '/main')
    config.add_route('search', '/search')
    config.add_route('result', '/result')
    config.add_route('wikipage_add', '/add')
    config.add_route('wikipage_view', '/{uid}')
    config.add_route('wikipage_edit', '/{uid}/edit')
    config.add_static_view('deform_static', 'deform:static/')
    config.scan('.views')
    return config.make_wsgi_app()