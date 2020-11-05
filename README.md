# parsing_json
모두의 말뭉치 파싱 코드 예시




데이터는 다음 링크에서 받을 수 있습니다.

https://corpus.korean.go.kr/



메신저 말뭉치를 다운 받아서 다음 결과 파일과 같이 파싱하는 코드입니다.


```

import glob
import json
import pandas as pd

fn = glob.glob("*.json")
form = []
for fname in fn:
    jobj = json.load(open(fname, 'rt'))
    for doc in jobj['document']:
        for sentence in doc['utterance']:
            form.append(sentence)
            
#엑셀로 저장하면 엑셀이 제공하는 저장 공간을 넘기 때문에 뒤 부분에 내용이 잘린다
#pd.DataFrame(form).to_excel("messanger_result.xlsx")

pd.DataFrame(form).to_csv("messanger_result.csv")

```



