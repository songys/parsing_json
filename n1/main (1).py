import glob
import json
import pandas as pd

ret = []

fn = glob.glob("*.json")
for fname in fn:
    jobj = json.load(open(fname, "rt"))
    morps = dict([(idx, "{}/{}/{}/{}".format(obj["text"], obj["tag"], obj["par_lemma_id"], obj["par_word_id"])) for idx, obj in enumerate(jobj["morps"])])
    del jobj["morps"]
    jobj.update(morps)
    ret.append(jobj)

pd.DataFrame(ret).to_csv("final2.csv")
