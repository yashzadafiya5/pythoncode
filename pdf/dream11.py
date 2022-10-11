import random
j=0
while j<=7:
    chooseable_player=[]
    fire=[]
    ok=[]
    hm=[]
    captons=[]
    # wc_capton=[]
    batsman=["raina","sahevag","hardik","kapildev","abhisek","kohli","ruturaj","robin","andre rasal","pollard","rohit"]
    allrownder=["moien ali","jadeja","riyan parag","bravo"]
    bowler=["depak","umran","sunil"]
    wk=["ms.dhoni","dinesh kartik","risabh panth","kisan"]
    # captones=["raina","sahevag","hardik","kapildev","abhisek","kohli","ruturaj","robin","andre rasal","pollard","rohit"]
    wc_captones=["raina","sahevag","hardik","kapildev","abhisek","kohli","ruturaj","robin","andre rasal","pollard","rohit","moien ali","jadeja","riyan parag","bravo","depak","umran","sunil","ms.dhoni","dinesh kartik","risabh panth","kisan"]
    capton=random.choice(wc_captones,2)
    wc_captones.remove(capton)
    # wice_capton=random.choice(wc_captones)
    # wc_captones.remove(wice_capton)
    captons.append(f"capton:{capton}")
    # wc_capton.append(f"wice_capton:{wice_capton}")
    state=random.getstate()
    i=random.sample(batsman,k=5)
    k=random.choices(allrownder,k=2)
    fire.append(k)
    m=random.choices(bowler,k=2)
    ok.append(m)
    wk=random.choices(wk,k=2)
    hm.append(wk)
    random.setstate(state)
    final=captons+i+fire+ok+hm
    chooseable_player.append(final)
    # print(chooseable_player)
    print(captons)
    # print(wc_capton)
    j=j+1
