import pyglet
import os

from client.ui.resource import ResLoader

with ResLoader(__file__) as args:
    locals().update(args)
    card_attack = tx('attack.tga')
    card_graze = tx('graze.tga')
    card_heal = tx('heal.tga')
    card_demolition = tx('card_demolition.tga')
    card_reject = tx('card_reject.tga')
    card_sealarray = tx('card_sealarray.tga')
    tag_sealarray = anim('tag_sealarray.png', [83]*36, True)

    card_nazrinrod= tx('card_nazrinrod.tga')
    card_opticalcloak = tx('card_opticalcloak.tga')
    card_opticalcloak_small = tx('card_opticalcloak_small.tga')
    card_greenufo = tx('card_greenufo.tga')
    card_greenufo_small = tx('card_greenufo_small.tga')
    card_redufo = tx('card_redufo.tga')
    card_redufo_small = tx('card_redufo_small.tga')
    card_zuidai = tx('card_zuidai.tga')
    tag_zuidai = anim('tag_zuidai.png', [100]*3, True)
    card_yukaridimension = tx('card_yukaridimension.tga')
    card_duel = tx('card_duel.tga')
    card_worshiperscarnival = tx('card_worshiperscarnival.tga')
    card_mapcannon = tx('card_mapcannon.tga')
    card_hakurouken = tx('card_hakurouken.tga')
    card_hakurouken_small = tx('card_hakurouken_small.tga')
    card_reactor = tx('card_reactor.tga')
    card_reactor_small = tx('card_reactor_small.tga')
    card_umbrella = tx('card_umbrella.tga')
    card_umbrella_small = tx('card_umbrella_small.tga')

    parsee_port = tx('parsee_port.png')
    youmu_port = tx('youmu_port.png')
    ldevil_port = tx('ldevil_port.png')


    for k in args.keys(): del k
    del args