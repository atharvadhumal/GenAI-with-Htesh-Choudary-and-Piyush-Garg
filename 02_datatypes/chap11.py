import arrow

brewing_time = arrow.utcnow() #gets a defualt standard time
brewing_time.to("Europe/Rome") #converts into eurpoe/rome time zone

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavour", "aroma"])
