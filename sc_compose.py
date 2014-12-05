# -*- coding: utf-8 -*-
def compose(hashex):
    msg = "Hej!\n\nFysKam genomför sin årliga medlemsgallring och vi ser att du har varit medlem i mer än 1 år. Om du vill fortsätta ditt medlemskap ber vi dig följa länken nedan:\n\n{}\n\nOm inte kommer ditt medlemskap automatiskt avslutas 14 dagar efter du tagit emot detta mail.\n\nVänliga hälsningar\nInformationsansvarig".format("http://link.to/reactivation.php?v={}".format(hashex))
    return msg
    
