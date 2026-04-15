def convert_iso_preds(preds):
    return [1 if p == -1 else 0 for p in preds]