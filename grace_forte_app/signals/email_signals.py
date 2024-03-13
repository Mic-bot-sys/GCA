
# Start Signals
def emailNotifySignals(sender, instance, created, **kwargs):
    if created:
        print("This Email Signal has been Triggered Successfully!!!")
    elif instance.isApproved:
        print("Training Payment approved Successfully by the admin")