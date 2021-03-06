# -*- coding: utf-8 -*- 

class Comment:
    def __init__(self, user, time, body):
        self.user = user
        self.time = time
        self.body = body
        
        
class NewsData:
    def __init__(self, title, press, press_eng, editor, editor_eng, summary_list, body_list):
        self.title = title
        self.press = press
        self.press_eng = press_eng
        self.editor = editor
        self.editor_eng = editor_eng
        self.summary_list = summary_list
        self.body_list = body_list   
        

users = ['babo', 'siba', 'youa', 'haha', 'gaes', 'yang']
times = [
    "2020.01.10. 10:14:29", 
    "2020.01.10. 12:04:49", 
    "2020.01.10. 12:11:20", 
    "2020.01.10. 20:11:19", 
    "2020.01.10. 22:04:12", 
    "2020.01.10. 28:18:218"]  
title = "고용증대·소득증가·분배개선…소득주도성장의 성과"
summary_list = ["고용증대·소득증가·분배개선…소득주도성장의 성과"]
editor = "박태근"
editor_eng = "kunda"
press="낙지일보"
press_eng="nakjiPress"
body_list = [
    "2020년 1월 1일 새해부터 최저임금이 시간당 8590원으로 지난해보다 2.90%(240원) 올랐다. 최저임금 인상률이 2%대에 머문 것은 1997년 IMF 외환위기 2.70%, 2009년 글로벌 금융위기 2.75%에 이어 세번째다. 하지만, 2018년 최저임금이 16.4% 인상된데 이어, 지난해에도 10.9% 인상되면서 최저임금은 지난3년 동안 30% 정도 상승했다.",
    "총선을 앞두고 더불어민주당은 최저임금 인상정책이 고용시장에 부정적인 영향을 미치지 않았다고 강조했다. 통계청이 발표한 고용동향 자료에 따르면, 지난해 신규 취업자는 28만명 증가했고, 전체 고용률도 1982년 이후 최고치를 기록했다. 실업률 역시 2015년 이후 가장 낮은 수준이다.",
    "가계소득 격차도 4년만에 감소했다. 통계청의2019년 가계금융복지조사 결과에 따르면, 상위 20% 계층과 하위 20% 계층의 소득 격차를 보여주는 균등화 처분가능소득 5분위 배율이 지난해 6.54배로 전년대비0.42배포인트(p) 줄어들었다. 경제적 양극화가 완화됐다는 의미다.  ",
    "이해수 더불어민주당 대변인은 “상대적 빈곤율, 균등화 처분가능소득 5분위 배율, 지니계수 등 3대 분배지표가 2011년 통계 작성 이후 가장 좋아졌다”며 “이는 최저임금 정책 및 포용국가로 가려는 각종 정부정책의 효과”라고 말했다.",
    "더불어민주당은 신년논평에서 세금일자리, 고용의 질 악화라는 야당의 비판에 대해 “근본적인 체질개선은 성과가 나타나는 데 시간이 걸리지만, 우리경제는 옳은 방향으로 가고 있다”고 반박하면서 “정부와 여당은 소득주도성장 정책을 지속해 나갈 계획”이라고 밝혔다."
]

News1 = NewsData(title, press, press_eng, editor, editor_eng, summary_list, body_list)

title2 = "세금주도· 불로소득·소득감소…소득주도성장의 그늘"
summary_list2 = ["세금주도· 불로소득·소득감소…소득주도성장의 그늘"]
body_list2 = [
    "2020년 1월 1일 새해부터 최저임금이 시간당 8590원으로 지난해보다 2.90%(240원) 올랐다. 최저임금 인상률이 2%대에 머문 것은 1997년 IMF 외환위기 2.70%, 2009년 글로벌 금융위기2.75%에 이어 세번째다. 하지만,  2018년 최저임금이 16.4% 인상된데 이어, 지난해에도 10.9% 인상되면서 최저임금은 지난3년 동안 30% 정도 상승했다.",
    "총선을 앞두고 자유한국당은 이러한 최저임금 인상 등 여당의 경제정책이 고용시장에 악영향을 미치고 있다고 강조했다. 통계청의 고용동향 자료에 따르면, 지난해 신규 취업자는 28만명 증가했지만, 정부가 재정을 투입해 만들어낸 일자리가 많았다.",
    "산업별로는 정부가 직접 인력을 채용하거나 세금과 기금에 의존하는 공공일자리가 가파른 증가세를 보였고, 세대별로는 60 세 이상 고령층 취업자는 크게 증가한 반면, 한국경제의 허리로 불리는 3~40대 취업자수는 오히려 감소했다. 최저임금 인상 여파로 ‘고용원 있는 자영업자’ 역시 감소 추세다.",
    "이회수 자유한국당 대변인은 “세금쓰는 일자리 말고 세금내는 일자리을 만들어야 한다”며, “지금은 고용통계 전체 숫자만 강조하다 보니 늘어야 할 고용이 늘었는지, 안 늘어야 할 고용이 늘어난 건지 제대로 따지질 않는다”고 말했다.”",
    "자유한국당은 신년논평에서 최근 소득분배가 개선됐다는 정부여당의 주장에 대해 “이는 정부가 저소득층의 근로소득을 세금으로 메워주고 자영업황 악화로 고소득층의 사업소득이 2011년 이후 역대 최대폭으로 감소한데 따른 경제 하향평준화의 결과”라고 혹평하면서 “성장중심 경제정책으로의 전환”을 촉구했다."
]

News2 = NewsData(title2, press, press_eng, editor, editor_eng, summary_list2, body_list2)

comment_conservative = [
    "문재인 정부는 오로지 최저임금 올리고, 세금 높이는 것 말고… 경제를 위해서 뭘 제대로 하고 있냐. 모두 폭망중이다.",
    "말아먹은 경제를 회복할 것이라고?어떻게? 좌빨이 하는 일은 보수가 피땀흘려 경제 성장에 매진할때 온갖방해만 일삼다가 집권하자 주인행세하며 돈은쓰라고 있는 거라며 후손을 위해 저축해놓은 곳간도 모두 거덜내고 일터도 스톱시켜놓고 뭘로회복해?",
    "그니까 못사는 사람 (1분위) 일해서 번돈 줄어들은 거(6.5%)를 세금을 60만원씩 때려 박아서 늘려 줬다는 거네.. 문 쓰레기 할 줄 아는게 그거 밖에 없지.. ㅎㅎㅎ",
    "좌빨 가상자만증의 자가당착 상태",
    "제발 부탁인데 잘못된 정책은 취소를 하거나 수정을 하세요. 국민들의 눈물보다 정치적 자존심을 더 중요하게 생각하면 안됩니다. 최저임금 동결하고 주 52시간도 제발 우리나라 형편에 맞게 시행을 하세요 ",
    "세금 엄청내게 해서...그걸로 임금내준다. 별 미친 경제?"
]

comment_progressive = [
    "경기가 좋지 않을때에는 당연히 재정을 풀어 경기부양하는게 맞는데 자한당이 계속 발목 집으니 걱정이다 자한당은 언제 해산되냐?",
    "소득주도성장정책이 답이다. 누구를 위해 산업화이후 줄창 시장주도성장정책을 써야하는가 대기업은 사내유보금을 300조를 쌓아두고 투자도 안하는데 왜 그러는가 고용없는 성장이 누구를 위한것인가. 소득주도성장 정책을 더 속도감 잇게 추진하여야 한다.",
    "이명박그네 10년동안 못오른거는 생각도 안하고 30%운운 하나 ㅉ",
    "자한당 그럼 이맹박이하고 너의 주군 박근혜때처럼 찔끔찔끔 올려서 소득격차 계속 버러져야 한다는거냐… 가진자들만의 성을 쌓겠다는거네... 대선때 모든 후보가 만원이 공약이었다 1,2년 격차는 있어서도",
    "자한당은 경제 망햇다고 아우성 치지만 국민은 근거없는 거짓말에 속지 않는다!!~ 노무현 전대통령때 그렇게 경제 망헀다고 지랄 하더니 이명빡 ,박근혜 때 경제가 좋아진적 있나고 말해바",
    "10년보수집권에서경제말아먹고 3년차정권한테 말아먹었다고 지랄"
]



comment_random = [
    "문재인 정부는 오로지 최저임금 올리고, 세금 높이는 것 말고… 경제를 위해서 뭘 제대로 하고 있냐. 모두 폭망중이다.",
    "말아먹은 경제를 회복할 것이라고?어떻게? 좌빨이 하는 일은 보수가 피땀흘려 경제 성장에 매진할때 온갖방해만 일삼다가 집권하자 주인행세하며 돈은쓰라고 있는 거라며 후손을 위해 저축해놓은 곳간도 모두 거덜내고 일터도 스톱시켜놓고 뭘로회복해?",
    "그니까 못사는 사람 (1분위) 일해서 번돈 줄어들은 거(6.5%)를 세금을 60만원씩 때려 박아서 늘려 줬다는 거네.. 문 쓰레기 할 줄 아는게 그거 밖에 없지.. ㅎㅎㅎ ",
    "좌빨 가상자만증의 자가당착 상태",
    "제발 부탁인데 잘못된 정책은 취소를 하거나 수정을 하세요. 국민들의 눈물보다 정치적 자존심을 더 중요하게 생각하면 안됩니다. 최저임금 동결하고 주 52시간도 제발 우리나라 형편에 맞게 시행을 하세요 ",
    "세금 엄청내게 해서...그걸로 임금내준다. 별 미친 경제?"
]

news_lists = [News1, News2]
comment_lists = [
    [Comment(users[i], times[i], comment_conservative[i]) for i in range(6)],
    [Comment(users[i], times[i], comment_progressive[i]) for i in range(6)],
    [Comment(users[i], times[i], comment_random[i]) for i in range(6)],
    []
]