import nengoimport nengo.spa as spamodel = spa.SPA()with model:    food = nengo.Node([0,0])    model.food_rep = spa.State(2)    nengo.Connection(food, model.food_rep.input)        position = nengo.Ensemble(1000,2)    model.motor = spa.State(2)        #nengo.Connection(model.food_rep.output, model.motor.input)    nengo.Connection(model.motor.output, position, transform=.1, synapse=.1)    nengo.Connection(position, position, synapse=.1)        nengo.Connection(position, model.motor.input, transform=[[-1,0],[0,-1]])        model.task = spa.State(32)    model.home = spa.State(2)    nengo.Connection(position, model.home.input, transform=[[-1,0],[0,-1]])        #predator = nengo.Node([0,0])    wander = nengo.Node([0,0])    model.wander_rep = spa.State(2)    nengo.Connection(wander, model.wander_rep.input)    actions = spa.Actions(        'dot(task, FOOD) --> motor=food_rep',        'dot(task, HOME) --> motor=home',        '.5 --> motor=wander_rep',        )    model.bg = spa.BasalGanglia(actions)    model.thalamus = spa.Thalamus(model.bg)