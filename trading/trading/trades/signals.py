def perform_trade_presave(sender, instance, **kwargs):
    from models import Trade
    # if not instance.created:
    #     Trade.objects.create(user=instance)
    #     instance.created = True
    #     instance.save()

    pass