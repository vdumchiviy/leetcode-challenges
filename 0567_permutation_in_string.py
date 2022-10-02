'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''


from copy import deepcopy

class Solution:

    def new_try(self, s1: str, s2: str) -> bool:
        if len(s1) == 0:
            return True
        if len(s2) == 0:
            return False

        if s2[0] in s1:
            return self.new_try(s1=s1.replace(s2[0], "", 1), s2=s2[1:])
        else:
            return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        result = False

        if len(s1) < 999:
            # recurrent if deep s1 less than 999
            for x in range(len(s2)):
                if s2[x] in s1:
                    result = self.new_try(s1=s1.replace(s2[x], "", 1), s2=s2[x+1:])
                    if result:
                        return True
            return result
        if len(s1) < 1000:
            # deep s1 = 1000 (no recurrent)
            s1_hash_template = [0] * 123  # maximum ord of enlish letters
            s1_len = len(s1)
            s2_len = len(s2)
            for x in s1:
                s1_hash_template[ord(x)] += 1


            start = 0
            left = 0
            s1_hash = deepcopy(s1_hash_template)
            is_hash_changed = False
            while left < s2_len:
                if s1_hash[ord(s2[left])] > 0:
                    s1_hash[ord(s2[left])] -= 1
                    is_hash_changed = True
                    # seeking is complete
                    if sum(s1_hash) == 0:
                        return True
                    left += 1
                else:
                    start += 1
                    left = start
                    if is_hash_changed:
                        s1_hash = deepcopy(s1_hash_template)
                        is_hash_changed = False
            return False

        # version 3
        s1_hash_template = [0] * 123  # maximum ord of enlish letters
        s1_len = len(s1)
        s2_len = len(s2)
        char_count = 0
        for x in s1:
            s1_hash_template[ord(x)] += 1

        start = 0
        left = 0
        s1_hash = deepcopy(s1_hash_template)
        while left < s2_len:

            if s1_hash[ord(s2[left])] > 0:
                s1_hash[ord(s2[left])] -= 1
                char_count += 1
                if char_count == s1_len:
                    return True
                else:
                    left += 1
            else:  # s1_hash[ord[s2[left]]] == 0:
                # if s1_hash_template[ord[s2[left]]] == 0:
                    # there is no such symbol in s1 originally
                s1_hash = deepcopy(s1_hash_template)
                left += 1
                # else:
        return False
    




sol = Solution()
assert sol.checkInclusion(s1="ab", s2="eidbaooo") is True
assert sol.checkInclusion(s1="ab", s2="eidboaoo") is False
assert sol.checkInclusion(s1="hello", s2="ooolleoooleh") is False
s1 = "lrxdxvfejdkrnjillizofhtcsnsaayremyicmvfsfuxvmlskswyfjwxdnotttdfisbfnoldsfaarpaesaltnvgrdoktdnxwgyblyshlhlubpeamxfrsfhtlcezzwsjtvcmzkpvfvmhphwksghfnzhbwogziokkkhgvrmndwsjjsegkdfobnecberwraetxwdxemzpoakgnovqpjgslmakuceqdorytxawxndpbkvsbalgfkreaplyrkbxwzfdlzsmoazxcmrmattzszqehtevafgiurhjbtfmztjgozkunklacupomjjafbzjerxlvgmnsjqcrsrbrcugaofbiuvibjmekhyddhwberuoaxfghtdgjwbjlziraohnmkhutuyftiptmdeshtyhrhtdkhgkzoxnulfqboeimlepwyihauwjsermzmefzlkubovxhrtkbfhopvhwuukkacivimrnjaxmpecncgxfelmcfgnqueelqssgpxpidtswwrrlusgwznwvuvdahajoxflexnctsgmjchtgfwlqsfyoamaaaowxttgshiszohczagbgpoqibghhawdjftrrgpuailqfpwzvytgwdyqfymihyuwhxzhawpoxafxvnwvkhwubjypxjnqjkfblpeoxewtjfnlgiwfkxuirhpbeyokyrbnmichszrsntbaxrdiznwfiokbuhkwvmhtunabqninaztpcvzptfjnhtxzjuupwvtsaateiuerftqjxqkljxkdindkrnsmuhouhpquabwanjeoyaheqgdkdyqsqdzlrdwyrakfdphasupvuhwvtsesrlubcapcdzutmiyyudpognnmmncgphgmfdozclwgvxhhsbxaexuenknayihkarjrbipmnujdfqfvvfbaickybuacyuutbarjsmveivscoktcpfzwlcjemengveudvdlcdjnpbjbimokldsbjlsdasbgjukkoeucwlhtmkxhbrnczapqhoyhrqaogbkeqsczwlloqiguclumiggrijlymcszkqnmgtzjcblnylpigzbwiynnwojnkyxnmgoodljmmqcprzznsmcruifltbdujttnpjnttlbfwlclgewsdcjgbtuzwsayatuqvmebtvihljkaewfnqbotnmkabcqsxbohqleqlrujvughzcurfuhmhfklbwbaudmyfttsikiwzbvlfwmetgsnxxlmjofrtfdfcsnqbyeecgzelovranroxccdaqyfqtkjxeqehjoeqytkaombdgfajafmvmqzzxfaiezovbzcyihaucpeopptarcwihwklrpvtkqnbbquqnlmdwygbtkstzwdznbevlyfivqflpacmtcsarbbkmenyijnjvwlixhmqrqrejwznxzdiqzrrfejxfmcdzmfkjvbwfmstilkrmvviywuquenujtcqbhkyxbnbbdoxgyjpxfucdmsecnzstjlsivelupyptdogsjepgjtwgoexaxjfduvkldfudwlxmnjyynypvdvgecyhflaiyrhbqmixmwgsehsfmxyjzvkioaexjbcnakbakbrvtwgghwhfsffnamcgphuqqxqvbdmfhrzxlgiunazqhfsxgxxwktpjicnmeaxyhyfauegcdiykhuouqqnybgxcazckmzriyzuulqeqtgjuawvissukncpataietvuwirkaifroelxsptnolduugufycgnvamsardwrueajvhqkkxkkhzphbuqbldukjdqcznwscvnnqnwxszplqyfuctorjcbucxgfctibwfxftrdliugohjgmbxqduvwgrdmmawyhfgkkbeojyxkoftuluolffjvygyzftmcuthegrxdkyegkucgnukwvyjqjeewteaivfoybrwaceyasgwxsznkjzwyfjoiqeclwlrnyqdxmzadkjvhjaeghfcaiyrjefpkyhslkeogzgijtdymtwcopbvhzcqficucdfzhndzddunzhnkmllhjrrjcvksisdphhmqcnsrlmyygxhlakemvncrogiljrtfyvdrujjwowwjxbjxpjhebvheexkniipvotlumxpjplncxsrezcxmyansqmarfwwtwngvcgqcijzrhvlwalkcdsrccschgudpahdvlunyzbrdfevmnoewvavrklwvfiilgtmtexwzfmgacugaalcxqeplsmpkplutliqairwtbytsxzlupqplbpadgsiuazxvrdwjzxpijvwytgmsocughjqwbsvozcfbflqgokqjdxrivnioxcgefxmkjajkwllqdcepegzzylflfqxclhsooylinxpalctbxsvbdjqmmcyqfgfytstbpmjgmqhmnnesgovyzwsatnvqallzdjrtetzdxhckykznmnuexzsfyncndzbqstxwppzjolipszefzxqoyjteoykmrympogufseghdqlvvipuwfzheescacwrbxkaqcutfrngmzmqxeeorppkjgdroxoqdkyaawrpcjtfxzlfgkrguphggygibcialnnkvlnevkbapazmpcguhmjcmizjsinmqjknavhumrdmjnbscndtfapztvczvhkpcowavszavfcwwlzdddpuliglnjucqziltqwlsibodwdcbmorwyyqcvwoesjibeqcgsbtcelowxtzryhvepjcqnpmigbdbuplezwgcqekhxzvsbwlaunotrhhmdrrfjoeyzwzygeypgpxonkzriqjsecoqdmeslcfgnzlwstigfxogzwrjznvgtrzjdvdiaofktlzpvnjftauzfmgigxuydyddabcucklupsjycdbdzdghkiryjrjuretnulfczhhwdoayrrvljbihhbmxvzyjxrwkpmxxephocpleznusehkxjgjqlalbgenuahcqzcbvnurwvtwvrvefnkdwywtokrxhstwwybamnixtlokktydnuqrnxylazddpvdbfhtevujagbvqkbjtcvedzrqpkwmxnsugrklcimmgbjmnatgmyyuvnbuffgjcvclkglhdwufxclndhyvoecrfqfxtmunjqavkrhyhlltnxwjsdzvkmxayxmgvsoaewlergrdaxssqtavrkazjkamfeyvttdytukwsqxrevtfquuanjywitzajgdlsgonmxjwxqiekadyohkzlowywqrmnydclodaichygaxhljvvlnbdpsweicfyntnxmaxotdnizxdfkhtnegosqynavfeludbsxylfpsxrnasizvozwlljokgirgewaskykpclgictznfysqmwpkyjntcvikxapgxupqewswsuqcnlajdndiujuwcfjkhysjltdbjjgxgnbovwzrcibzwasjoitdrpyureacgvdupxpzqepymwjxruyxkjhlsgiddghluhkomqmpzbucxryifzszpmknuakmbmieksazgsmzpuybfdlpqlilcqfewgqkywbianhzgizbgkruslhepkllojtoewgrhxmqlziexxfacuzjgvpgbusktkkctzyznwycsklkrrjrvbmxbhrhpwaketgqdubkavullzlhxdahukoajvrjfdmcltylxjllnwycvbcddpxidjzhkpwvlbrnxmnvseioujesuieatdxcptqprwaukeqdodaedzbwmybatapayautrbyayjxtnvcniqleohffgxgsogwslduzbpkaxtxwzstjftgriebrlthrhplhpqtglcjzoospsolqtofgjttxzpdceficxvxvzkfbptevvmjiviglepvhatglwgbeywcsgrqrttwjblyskptgwkhlyudcxolbkajzjeuvdbdourryxldpzlbfombingjbamxelfvqnusymtussovzxkyemigegqlqoprynkwuwhxmvkacwplrgsdxbcoykxbgfyfuclxcaxpzqgukwkbvrcmzvuzinucgryrnjvgysihixhcknpfgjmagmlpihnnbniksegyxybmgwsqgitctffwgudyvrkhnnuqczybxadjfzbakmrpzqgsfdtupbrhkyqumimuwwtwaugrpwppfcgpxkumziermyqqrihufxtfklmjsipuyimbrfatepkufdonqditpcnxbanfxfhmmwutomluagakhinnrnjwamaztgozkpwyxipxlellbszvgewelbwvkxxvrmtvuiivdgdfpwwuwvmxnewqkpoocwbzmpbscymmrbrtaazhpxvktdoukayngafglbvnmvstahrlsxwumubkeceevztlzwiyfiwtyuiyjbghofotfqpygwvgzlzieajohxtnfwfjtpezunhtezmgoijeullayhjlrklddeiujhukyhgvwhztrvrdcbxhuvgiwmjwetjmwzoipopdegynbwjbxblgkgcbeljnlmdogjlmfcebkpsdnojqxzgmmwprbvjnvghxqbozfmbfpohiwtmdzumxlgtspaodgmqrykogolwgvklwvcxuwqztapgggossaayeiyramtvoicssnfouddszofopvrmkhyihbiuabdzrxflubidzkorufphwqryyznzlcgffamyeacfjvdkoilbvurswxuwbfsgjqhsajbsbvzxwlsazxgfmnlilenuuowslmlrrbzpkmoelvhpvqdwuutwdsowwldmuwzvouqbynybgnvojeyzvpsyzyrmreeahzutgbgoinadnfnctsezjixjdqkrleovfjydtnndeuycghsuwioyqjpdwhqtgrazzbxfwgykjbvewxrrcdykuomrlhamlhxzstykmfncbbkozncogbthvdrttafboicppqgfuvutfsrdvpnvavatvpfcpoczukoyskqyinzhpdunoxffvjpfxyxnelalhnwmzjzcjbndqkutxlekciqzxsgdynwvfuhkqlssuywktmsgbrazfedmjwfjuoxroanbipuiilqpwzdcbalwdxxrpdkwdrjzxlczzbwxlecntxgstkhctsdjocleuhmstcqnvlgkedyibdcdohnzxavsdbjvxucnuirrjenhxxtsyunbydyllkijehpwffykdjygganbiypiogebqmsndzdkqyodabqrwitrmhwkaptgrtfyxfjtdvyhbjybfftugtdocvomcsfowxbdhncpogbyioijutjgxirsauzvlvjktllxucqyniowzappgxvngghdpdlyrzvfzonmmijwxxbgvaikrswfefrruptiabegaomcjjnkfoazlyvdvppywcxjpjbxauyejrfixnkxflguuqwbuxocawwuhvhlvrjcklekcwocblavcitgpwmuxawxrvgiibgozmuyzvyonyvgyxlezcajxchiytjoaheozixofdgstnijliogyvfrlmaepvifdrqfrdufbuhqjqiehnakvcqoxaskpbrrgynnkqvnzhkbglpaeqdvqxxghuixoydcwupbvpkelrzfwlzenzoqbulgvvkowpddxcpfrigxgeuccqvkzkfplcyyaqsheqjwosqsevbuvpglnlhtoieubioskacdfpvorogamnbwnajomrdfrzgkufouftmdiowtxkmbktzvvnegotgnzmklvnhmwrmajxytpexwymfxcerimsyzxhraehnhmshkwmcvaufbsycfcdjacgawmvwvmvybwqajhflxmbjenkeyvyullqyxotwkrtdgglgrlxcjiicnsutkjldirboqlmvfrlllxtiquhfpxhczzrmumznjpwcfmwmemltqvkhskbchpwhqruvqnqixbtorkrhxomtuybgudzonchsslxyslgzecpdavfxescyoitwqxnvcsepeonbuzoyoeypezouczbzzbnmzccgkhmwfbmeicmwqjdegmbbckgioqwzapatrbeedksjspndjlvljlqqnesduhbbtmgrzpbjhorzhknjpkrxznthoxsxxrnppmalnehvkkpdoskffkqithkqjgmtbxgalntgispxkgqvhxcydzfsdkuwdzytkolzmywtsqqbkssplynomcsnfethndaicofgxsaslupmgtblvwvhsamejhvdqhuijdwglfjpfagvtjmmghikfnetdewtwqgsjwtlvwjcifwurvaqwbcrpiqghnntivzzqdvuqtucbwustfdgpqvvneouriwiqxsyrultkiysyqcgijkiqjrxnfwrxahlkrcnodyjtfybfspqckojtriwfojgpcetjayrgjtrzigvtzosmohlywfyrbtryxhlcbhadacpplueillitgruqhexwcvhxpphbtksuirsnjnxvxyyiibloqmrevjlkghynenizwpkzduifnlfksipmljdujwqafywlvagomisejmbrzbxnogrdkikdvdgfwvxdoxxahtskkyonwlaulsrdjzokijupfxwdsqbveyieuwrohupopshocaeqdnsphawwnvrzkyzazdccnyodxpnuvjshmkrtmcklnqyeoovlexwksutsvhkbrhjhhodjidvkejkkxtvqtcpiiooltimziokpzajzfvpylcoxyglbkrglvnzftsmzmxbovviavuxezpxezuxzzfrefvbukfuwzhxzjkfaynfcjvkvbndrdjqdhnsrcxicxsxfjsdpvsmwvpqijeemnknsofeqywovbdpdopggrfubumvranfzpmehzuqgykddajkwqllyhalnyoylkyoczxozzrebnwljnbxvdxnaprgqwmfjeoyozqwqlwudlxjpuukrqupzigbvmoysjzpprcsusrzomywxqfpqomtztgrfggyhbbceiniofjaghnlucvtfdupgbhbvnfvtgexgnvjvwdtyxxgxxvgymtfigraqskxvnehqohwzqzkhxpifqrutlytfverrlbdwfqkiejvatuzccuxtousmxzppnkngxanzjhugytabydqynmnocqlcdxndwohtptktjdrxgtkvqyzoimgmsomqtnebsdvvrdhcalhgsuoglebfdhafgezwjnmgoshzoqffbtpilpberqitxkzyglpdkcwwvpdqjzwcvqiazhrurnesjrzmvwvdboouqyfhyeziceekrhncfjhdeumvxywinudsfovinwxsbconemtexvfafxhaerjvqnkchnsmgljwdddjsgcadvavlbnikfwvdsckvluigdvcfuezfxxxkrylxsnhwuduhfkdakllkawxmyqbkbzcqjmsbgzfpojtlpqvgtqlmwurarmavmmiatpfxvfzfqacptkhjgobtcsnazpbroehpizwtpmrclahjkkzcmmjznsyaglerbnkzetxrojtsqffhzliqwzdwefypaotvgeiawuwxxfkwlbzrntcaloqbubnyjdnsspmmlckzdpllmcncvrkdqrtmfbbbjsmuamsiipsqzexrckpcpnfnhjukamxctwsbfrcuuccbankpotvedkkyrmbttbzasydxkszzdadjlzrdmzbqtsqazuxeloeutjxdsciiugbwvfvwykptjbmrlxkqxaytyzubavioljyymsmkdzbiboaosucwfvwovzwcblglzdwuiffzclexudskropugxsszdttwruooehksqtgwabwrqxmiqcidjpadjbyldjmgfghezqzkqolfueavyousvfmyuwaaluszwzkgalilmguoiecvhsawptpskudkmvbniybaslympseyyinueidogmoiedkqvuoywnduxctjjvjhcphtaddsasmzrxwvfxkaypozvnhfalmcwvqcaeszthvbqzmdohdeqkfdeeislkblohlxrxqydoogzevgsbzhgrvyxvpgyngsgqzodgrrtqsbnpvfhybjgtuufmmmsekzmuyuejpjtuisqkrptauhsjcllecpfyttiapogqylltbjhzrjldccfybxsionmqpqeyusrtastfoqksshmziezadeogrojwcanijxknuvruioetfexnzfejkkxlxrktswgqdgkeznvyzwkjlixlxxprkbtskpjezoycykjtxjorxiydrgvftxttaciifiifbdmbhozmuftpvekolyxcwnzhwgmzcsiumegewfvyxwaijlgwnjpxohsfkuxxfytbvrkcjzlnxmmcgjmpjzbovcppppmpuvfcknlkyhbcaevgviusffgceekjwhswxhupfrtxhwhjmdtiicppzkcplcqaifzjzfnbbtistgucduxqprfughepxnkzengymokugzokudxesaoflosfcxdulhdqlhebhmuogzkqqmvpsrnljwszawaazgofirmswuogqzdbezgfhydcgtcmbipuuvrzzrlvsuxqgesprlrmdtvzukkyksflpojpmfkurnmjslxvkrqbknmmeavkiqowseqiionjffctbfgvdlgridoowjwflmdjdjpziiioguaspnacxlwlyosixpbxukglrnkzjtcalatqfxqrdrbfqltsgonoyzxaittzathzvrtjpmbnbnbuqmxfcwtxvnafhiksmbjxpxfshqkytwunhflybohwzuvvpwaqlwdbxnnzdnpikwnaxjyldyltfoiyqvhzrysfblphtjyaizftfmgbbicjfvbbnzjjofpymyrfmihrssgxontbmugivvupgczbajxodcdfutzydnfzwogncjrnopjsxkxzpxehitpeduciiiwiowxlbcdjfekjpzhdlmtkckhldpwcqntqnoftmjphqcfpydbmkpgwjpnjcgwwshltewdooxmzmmhwpjckxbrcwismkmkgnduvnbnjntvaaasxocisoreldzcpmnftluzqrvxpftrrvabdojqqklqvssptacdcnlejxgjyvreamirjwvlbdvyuuolbcdgoihylhkpqcuokyyfzzgldesantmyoqgcbyrkdzhhteybvgbeeektccdgkvmmywzdtaspyuilnmziledlzxuhpmcckyxiibjdaxgqmxybpewnynlwykabudmtmjwoujqstusxfkpnbhgjqoxxhxcahezybokuanmqfbotwkagqqohaxytqmeruwakokwomfnrdefuljckiixahakaxsdyojvutmdmgxdiegvlblyhogqlewcddesebpzleihfcrttmkewoalaxathwluyvvfbavhjsqkttzodstcekbpnthsvprfijukbuvtlqedjamwfahjhvivcoarduvrhczuxjbfxzitlorrntwebjauxejwpswfksxbtecdmwvtvjgvelliisqtmbfazilmmizkbqiifokdaajotapnpkqhdgsmxhtndlupujojefwkasgsqgbqnhkrxbfunnzkfdtnlisryccnoobvewvavmhwejomytxxoclwutmthshxdddpokdprsfumpcmqhbtwlmdepchvsfkoyfzlsxnrmmuxlktunydlndafnvwhkymapyfwwgkljzufstoofyguubmmhgqplgyudbpopzvsijjerphhgyqqubnkgqlqhaiyaulzufdrarxaruxhbzeowebppjirmrnffrwcmpxgpeonfndbeivayxqttgjqqpizyuiupftoyvaxxxqqxdnffhmfmtcfkocawihcyopiaxvjibugwitexixqxsuxyubcdysmgzelhgykjfizyuvqmiajlokobiwmnuggqaspymnwfvorlpzjikffuctkjlpsrbbnzpjqgxxbjfuuqkkvscynswjnmfrcfwwjeqntczherfhjrvgbpiqfkhsgjirldsypktnjphrdiuaiiuimptnqofmiqqlqvnhwiitgexcjopbshfubrlsdbvcdfdtoufxiphxrilhemygjytnzvabaqjwbckzbcpltovszpffbzvhlbatguhjufkjd"
s2 = "ylcotuazxfmsojotjtnjnbmiestmchaxbgxkimkcgtcutoqfunbgnastygeqvljyjnzwssxenqcqmlsfsxyznxqauakdjcczivtdvzhyfyzzzolhqfkaaazkjznxzdwicdrhlbxnwahwichaymehyqtwimnxpszgpdpakeuyqudenyntlpogkitjklxqsalvcdsptrhgdpmuknnnszmbbcroqbasxngigfnuvaehxbfqpmvkmmdlofgemxhordbctbafsvwutdnzmemmvviwubpgjsugexoevbbshdhguvhhvdkstmwbhtygfpzsjuqnxzamcunrqpmceteowiuqrstiqwisnfrwjhlbplwhlazvkobcbzgtaszyejkpcwnpstvsydjfrastxtxgsaeotdgrljmjtcykqvmcwoqjyrsuduekjpmijyotoypocpadvlzlxrpqojoboyflqecaqqkbkuugezkvvcvkuapxiiommosbwnrzxkesrsmzolwbtkrejjmidkbjlleqjlbwszdujsvryswyjmyetbmevrnnmosbbrdjnrfpjunbujpyvykqvwylstblxsqgxfaiiaxlkpkqypseezubvniivhpuzifpdylyrsvskexspzrjppzhkzkhnthtiwtwpknlyyqkclkplsdxtlxcmaplljxyidzwtykvtopfqbckueypiirrugnpvzraezxxmbexalqptvqdyqehyfnvdxmfazxkqzhgqkjdwqqmykvyhfaojgltqwrsesothqrrpdgmepgxtwkgwkxzzdkagvvqqhcsgxeqkajpakymxhybbxvfybgydshwneensnehanrrpkqkmxnyizlficycvywfdvynbxbxkleuhzqjslbolebykvqiarifxbofieboyollxqukpslzlorwcdadmbalgiiyarhkbevhsydredoafxtbkbgghrqrzlwyxpyxsesqobqgvdrjnrtefywdscecurexmqcvjhbeareyrzskicpzxslhdsdilsvdzejjnzuasswomocgmpvxoyolkbvsyvrkpfgdoljgaxzmjrzbsdqqferxhntuklenqcofnrcisedichncejxujhkqbluvckvogiprrmmqmjivomhhduyhastanololwdholknufuipjgadcbkyfhhwmlspckizotmqxstturxhvbopxzatdbcbftsfkvrnliswnlcnfjgztqiilhtrfshrczhwrdgakwyefdcregeybckvuxgefzqitllufrcrdohjrnvsliidhotpfegytotpjgrgvxzuxxmfqsslvleslloegsqiniesztdgqoniyperoecuubmkniqxdrpkautdiepqsfgyeyhcpywybmqpicoxjktqlhdowlzqnkywhbcszahuhdzusjrlytjajkhbekgkhfjhyehaboyodfyemvbdpumpwpepllwnkglmeoeutllgmnefdfsjjrhwncdjuoglolgnigesopzcitzmublikzvbtuwfmlixiouohygtpecaqiarvlvjquhwgskivqnugscbhwbfwczbomoyopkmcfawkptowxhcoinryagwzwqzrcvwqypuvudtqqootykyxjszfnwamnnawsrzxujldwqecjvgqasndukzkhjlglzafuuzkpdopxvzbfztszdbixxdhwuvtmbpgagodfvbkndlfuqsszddpucpcnkkafgztnthrhtviyusxpmvrmxehzihiloycjtxitiysabkskfgadgtanjgwtrtjblxdrpffwxbxxverdeaocyvtbiuoswdfslupbvvljskyyafmafpordsrcxgwhsrzzavxrxyalsltbgpazjsnzszbodpckrbgcswoisqpxrdqpyrfrkmzgnxkmwrsrjpbxdsygiavwrjtsvdrqcqdvcksifjmkxgjjbdhhonsmeeugggzwaehrkksqyuxfiujqzymvshundzkwufqduffudyiwgsmsgpcjcjcjoifgrtzcwzbwugksbjwnagrdkoyupijuususnidrwhutyumztdjhkplfoidxcpecjonvsyyegvgqkkgiftkpoiilavundmhfvylqyvmrsumbilvwuavxaprngmzfjmxfvbvifdujwkufbgdxvtonpbixlgwhaqywmvywqffjxemjyvimpdspcypuybsyplwpmhmoxjqxbbthncmpgtupboupshzwcftfezekfeqbtnznmicivderihfnhzgwnlngzaxmfmguhjzbrjnuvhfcbwbmikizkcrsuosadtdxtvybloevrgbvbqapepuoagfnbghvyczrfuoxfryilptnqvvekkiafdpqxbeebaavhaxodgignoovzdslkjvhhbfrcbyqkxdfpycxxbemedznmybhnmrlbtyaslixovkagqzcrzmuuqmnrmsbczuwazwzbpqjuoztiotejzfhmjdorvdbltqfkgannctbfwspwpplzlrwpxtfknwohsjwkypnccvkudgtkgzqcgrgpuvuhbdbhpcryogpuzozmcnsvrnjnjqimdozemipvdmurucidhtfwqfvvfvdjitdnzguxfmhzpakfacbodntjkkdjlgarjpdvwcmeorpgknauhqmdkbwosxgdgffgnhmmgnmggiemabhzlthcaffclixppqpahguysacoqroiekpgiflcaqkkzothgyfseissmhgknopogzfinuchyfwjsjuiiksttqpwjlyimcjnmalpqvbtsldznqwugkskikroefgqjnvzoplgfkzuqqyaalnefuircgrhwbshxunccnrdldxybkrpwwziakhemeusnxofbqqrkguncposjyljhbpyrzuesxxanbjxmuuabbrwezrehgfwqrqyflmmlydprpfuhecyqvmnhdrgffpkfgaixkrpcrilctvthuvezrudsmlnexfnkzubgbzatfcjjguufflaixwjgvgpcqyuxwsfnowafnglteueffzratxnqgibwtvcygoppgcnblumxfavizherpzfatmrrliswqegsdykjpbzehnexbpmgebrmqasodsgxodeqfwqwnytwtbkfydtizloygnlilyujxvdqeoquovhdpsnbltlopwhjwqzzwstofvocpnmckjlwrzaxrmvbfptucbnfvpqxybsqvekqugkcjcdcdmueoovkeyisnsqlcowimxzuvwpemluweeiuesxzlbrwehzqprznyvpwsezxgvafastynbrmuqchfglcowjvhevwuubhfiormhtlrhpeytnidyzppobjeclubjigdrmjyymyxyelbprgohpberhuhcuyvpchxqqdpgdnfgtmauvwidlvmlacdqycievmjdmbplpcczwiitflemhfesyhulkgnlftsyddxpfjispiebmzafbqxxxsbejocgiigvrwmqfcganokzaurismihwnikkmsdcbmfyfcuutrogtjlttaxnolsieihxvubpcfmnfnaiswjaoumfhmivzpbrraeftyhgirmrvyczfkssdnqpuhmjafvpnttxoixiwejurkijzywvanfxvkkmgqtqytnsfntetauncecthzjxfqrafouhagkrdsuxcxnzqaiytfdiqtwxkmhuhslnditxhjmmuijagmrrkpztwwftsvedtdtqetluqmcepvisnwvsonkxqelxiatbhhncoyadghlkegavegncnzcstexayayoupgwfvxtcjncpktjivgruxslebxukudntwhaftyevccdhwodugpdrqfwpzpztvthlmhfscdumxqosrgfswgmszyqsetwvmfhxlhuwulpvcsosqrlvzklksgimahvdaoxqakuvtpzvfejrflixyoyvdyywcfakndzhrvbdkrillejoicbpmhcnvpyhcufaezunpkoripsbcyurthkvnmkkmjsvvbpbyzwcjrcoemldczdslsezavblhzoxbbyjfuhxpbckhbkpkcdmtcvudsoqzbnegohzyhxwjsjiuzdtbjbegkbrkpohrgezmtxdiaghrfrdavhidckgmmkspminalblvgbauwyznpbtfpqzjzzlvzikefcuahffddmbjqpeflwgvsqoxmbxpxadaglblgroxqwgejpxzptlzwyfuhyziahpsyjljqyzewzhlfoctchirzfoxgauqaqmgzjeaktteinwhjtkxsnogefibirkctyuxlygmrarvsjvkytfdqcqlydebagavluuwgehlvuhcbbmmkrdlbnyqwlpnkfgmjktwuwtwtgaiynackkkvsbnkjrjznvmfeehzaorkyimgemzkwjzsejtzlbrtxspqhwjfsdbikpitqdissqjjginuptmrdhhgllrmxokekfldwpgzbwyfuctfohxrhehjevtbeiprlorgbuzxoogyqdvfgiblauogzefsxjiieezxqrqqltfvpasjefjobdqwdsizqntjeianpwbyxlxuqpasjvfrccwaumnvulwzfxqqkvjazxnicvkyimzfyhatigyhinvdqswpddpesgxrhdrpajlndymewtjpbmbxzfiqhviypfdyhlkbqjszxnkiehwhiezixdomsubvslkghkkxqgxzqnrizzwssgdbkgwzivfqtpwvzapilhmxpxigjojiosnkrrywoyjppcqgmuzfadytjjdbtrxeviprznshajjoqkjwdxeouuvehkszilakgorfcgkbvkpiwdqjzanxodhancltmjbjkaixxrcwvpccmzczysfokecjsaurtwtxgdogvjwkizbyoahrbvlsomdoxskcmvnorzzsjgekmdshujurhzowusqnlzzwvzfjzpmpnphoaockosikekbhqgfsqxqwtsuwmrieviwbygbgchtawboxwkhzyyosppdptngszaouukrkqgddofeiqsvcbzbnrwebcgtriehdhvifzxfjviwooynjzugjhdjstqszleaklelphlmippragvevsbkklvhluozuehemcarroaftzihnnuadpobwmvhxiouuwsfcphevzcuizvpctdjkpwhcttehvaivdxsvesgpyovtgvqngkppilqanxyeajpjgndkrromomkqfuwvnunzdqprzbgireucpvfimiyfrsrfeaibngfxhjikrktqcjcfbobbdpqrinprlmshfzyescgoqkpyhhujgfaasggpgujaprhjbouizljenfhacaobtvbwmdvilczkugwgeytzayoxobhcwgyzwsbonvwfjfltsycnxltltmntekdkhahuvwqucmtzsnagdmgflqgpybsbsfiuxajtrjrugpxdymrmjdllqqsgcaqvuuokajeubdryouyopwnmlqqtlfwyngxybrvzhzxvqyigoqcziemctkggxynbtgnlegyygyxndkbondpofznylislptfvxngrbctfpvyxlooujbccupycdfmvmailpyosezhkrctdxdycejuvvyscfhjnhdjqetmpmdnyhhprqaezkcbjjaqbekiutcfenaahsxmheisbvvtejkpxgoocpcfozswqsswvdzprzvyyitspufrwchskadjmrisuxuhxnnhitvfkwqnzpjbhzzcrbaxqapgcbihkifiqxjvopnyelulrauegwbuqqaoscuoawirzpfeidhtwqcnujbyrynokbfajnzjtctocfepkpzisckezbtkuqbivbecenwilmccerucgcnboxpmgsoojgqtxevhvmzecvktucxbjmirmqvoiebyhkzqtouiaoojigebampbncmiaqojbkgzakijdahjmtufwcxrmjcqjfzbrwwtnctgzhztefngvpwtdnqrrevzctxhkzckugtgekrkbmglenpsknjcvitacouzqpiiumixtpfqlbvzsylurbgytsszhomhnsrcccpczcqpprcopgudufouncsynqjwwtdqnppblgwhqhldkjmdsfiqhgvpniyeznnaxduqpwfdbhhbcoisuphnbynoocelojbqvuxdcjvwxasnxejjczuvrmrpcklvcijphbghcnbevagdnqfykifozsohueivxydchtmmawdaoiywhdmhpkkhtgyvgtdbgvcedwpocfbuibbcjqpkjlzdjsbanjihuwwvmchovjgwunonvwkqjdqrjkppfekjcehismyrbwrsikxuthwtyyzsikpdloayjkwbubwuuzyueyhpnbljukmqsugtzfpfyofptdoaxwtfebwqyezclnijfhykymgmyjadsxaxpzhaiqgqkygamatbpaaaevtetyoosbwvhferwvxcwzayfpfkgyvjgakyqgouhimcyccputtsrwejwliaxewjaedfyxhhovvdwiofccjjfkcodahiafzhhcundpsdfmbxlfrldyceezushrrmbkboaneauydlhrhhqfslwsssflzsnpmtqgsexgxvupvlvuucgnvchsayimzqwhegmqvppzfnasralodsteegzgdkabhkoaaiizjhxghxdshwqxpgbpppnazfchlueyqewpazmnitxjhxlmjfwqubyfpzrxkcjdxsnvdntqkohgsbrozewitmlyxiscjmgyprgtgkqzwryyfdptapcnuhusbncjyusndwbsxuwxlewjcmskculeinswcagtyomdoaxoqnirgsgvrqcsofzzsesgdjmwrnyybjesxrebxkjappjtrlloiruslbypzparqurtqzhnbeiraojtebexzzeofeqwiwnxdrvawbsnhwawncywlyrvmuwtdiyvevuvvndslhgrussnpzyqlmsjhzeyufdrbqkqfpdnnlhbpsgyswrzdfuzqhvftadiqeslgbwcslpuwqkdmkwqdaxuvuthcggpgnoeardqnhrotewuypozgmuzfxhqinipomfkydmcnhifpmrktzqlncoucbpelwtsrcjjwphnglgcgsgqelyqbeymotiifnybgatrrpbowpcsegimvqkmabnlbensjotxxetwhosblyxfitocmaokoadwjlvkgzoreyjkrpdohzmxljdrdzjqjojvbiyhokaxyxfikqsthjoamkxhkxymsgvklzvnnngjasswsbyfdabvfyjhpijkfwfiowtdhjciirqrbrwdukstrlirczvdzkkshfdkioucqtfmihpblqxwmvpxetweoifqiypthdfykdrkbwwcuyuygpqiqjadwypxtdphavaedauplrxwjxaitcoetjbwvhpsizvensphpexdvqjcxldpgizcysqljarawvrpnozhvslfuttphheiswsaxshbqacocmdkaoqnszfcdgpdqxezvwkphtsubkohnpgrdbjutfejpobxckjtemroeidwyzduxvbzdpqxkppvgusikpgozxttvnpojlreuqnpmjfhbmninaqzlgbvhbufgiuadefemupyrccczupdhsmwspkhhhaqmyalgreqrimamsqfbsvewaiebzffbcmyexchfycyzubexlgdhdafbujkbosnicuahvuajszoqmwqpbucusvdrteemrwvshfeuecdaswheuyynczjkinsnwxxxibgqcgcaxmmvdqpttyobhwgsxbuokjppdxyvqqtenjfbdfcrbdzllvhrlnzosfhsmyknjddmfblggrbuhgkpxxgupdbzkigbvemtpmnrmowkrdzegfpxplcwgybdknmbwyoyzmhvztoogkmrluykcrwioyhmqctnfnhngbmnbvgnfwtbvtudefcxvuylmchgnvyorxdywahexmgfjifvitjsbrbngoetpnqgzaiplpgndlitifeclroysuykbotgbszfnkhoiulxahjjwtxxfmozfunexiehijvvxtzwtdslklzaytplnovuvycxirfpdkbuuwsmsmqoqjfoodvbaavdraxocjfgdmldvhdylgdbzopxfgqsfbwatyuzusjpbfeqtdwhqmmzgtvokrtvkhkvzzxyjyoalgzngofigysifhsqwbcpdhvwvgsuefqjcakzujhnrkftzbiqevokharafvehvhqocetzwyjxbuwppflibuzgtifnyczhjedujdiyrqnbscqapnwulyoosuddqeflcrtbukvacifqivlonjcvsovzzhmnmoufatkqofjmhjrcnbkcnzaayzokqgvwzkjybnfioqgtkslxzfmyqldbofuyfqsevyolaumcjsmfxpdrulslchkkbaxrwjczxswhaxxumjkicxnvhwtxonipuogiderovcrhcyrczcubwgtyeeyvueazxseuhupjzxesveckigahupcdxlztbphdhdwvjtexivbkxyrmdsypabpqxixbnseiibnauhnbxqlkcwrvrmtdpbealttvvelqifmkfsjzhnaxdrgrfljlfrnqtcozuilmgudlzblnorriimmmgydrpostalitfjdxtdzanqwxfmdvduvpjtmbsttaegjltahgwlvhumxzjcrmbfbqxehmbvoksjlfrvnmchdcujqiazavyotzcksxrtlwzrbxdvdqfordtidhbtdjrpxplxhwoeutsevzvfthpscglynwujnjqgonhlojbjhcqtagesfxoqjcmvvyapmwnmegrttcauutfkjgqbgkomzhdnfxqbhlrmnznnqljffihmfxoziojgltztgyohzaxrqzvxnlcwegiodkiipzfgrnpdzxngspecqbdsdibrodbdbzezbgzfnbszvamskuojtlszltgbleebgfcriskbvxdlinojdqnystcszubjggalzaapkhvwslcgypmsrjydmnflbntzbykkbfaixyhuxmehrvxtdvgjimekmbsnnmkppoqmitlmuvadzyibbakinnaelbgpjnyvqjovucxpmsqtxiaxdyzftuhoetpvvndjqqdtauurgatbdshriepepbpquwpbppfqccgnbbmiaosrwvexrgrpvbnhanujhzyvvpneqexwmtdlurpdmhgivbtourwplhcwxikyoqkgmfyrtagybcgipwrmcooirzpaminzgfdnftdkgcdoemiatlwmclzbfthmkdjtainbbhbbtpjzybxpabusdnsbomrrwicghclcyhwmgknisoppgzwnfdiqtxctvitpujafnagwtippdmbfjcempupwdghhcqngyeszyicncylpfwrleyhjrxkoodcjclwqpcwosoirkchvieljwindydeiebtcouwxtiqsitutxjyzccyusxyrqopdbgvxgxvjwykgliphvhfoqxacgslyvzxczrrgvxptyndcinoecxkmdfuvzwukskhwgcchczewwbzsrcalgjxxkdaawwemrdcnsqpqoqfreelretvrtsuaunbsejbynikzslsvorwabfnkdnurzpcyxkkoqfonvrbwnoxziwuzgyqlrduaeqeqrxppbajzbdchrzwogyoevzfizrwsdvdctxkrzlkaqmdbeqchnxuhitdczebntajmypyyoxcmdfcegpnxwcoyelfpppfiupzknpweyjkddeinihrakkguqfdyfsapabsykvaeqcgehwwkhjhfeumpfkdmeuptxoabccuwusteyjzonatqqejbcrndcaadeskdmdbrimrhnfradkdpbnyudldgiuboguwslgxczetqvmyhcjoqamgdzgmclemtimaoroartgbkwgnegxoordytopfsakgovafuclbjvcfypkpkoqlqysepkkaqmtcbwtnqkdbqddhzenqkneapjqxmboiaeifwivjqswfplbmtmvlqsbhhbgnrpaqaznoqiblvcvrylsmvvtuhlyvonb"
assert sol.checkInclusion(s1=s1, s2=s2) is False






s11 = "jqowgtqdokaxwlqdhfvyxnaflcxinzmwptndasfcllrucjvixufbcdrwcxbjmvwmjzjcqnugddugkaqbirmthedbfidisueqruimmvetezyzjvyqzucdlrlicqldmtsrluhphqrwejqbcgafhqxfxceibvshmvdjubdinoeqlitgnhvjvbqwcvdhncxognwoaeyojayyrzbokaxsihhkzbkvaczlmepzhlwnyzdzborlwbhicmdyieiwarxwpzgukknkplhmkciolicttdsbesbkysnpwhhqmpdctfqyawxxbrjmgbefhuajwedaingmrwfdptobbkfxgupczsahmxngmupbolysndbgswzlxldjynxrooiszcfyhixupcgudalteszwwkrhipqmxckzxydftkoxsmemggcedizgqihcjnbnjaduhucwoxarpachkqmnhafddyhaoqkeskodukkgnnejjskykgwfnoyspcjgvnbjmxdnpvxjbwqkokzchcvddbuzgtbackxevisusequrqwrsmeqbffcfzzzdqvreeydfygkmkzftzgbkjznqqdpzanpojqhrrghmnmmjsgxnozjnieuffbsvtxzizwhhtcrszyjwlmbxklakzhymzvpuuywpqksiuifkshzsdsnsgdbpmgvinihwykzzpoojukgltdcvncerrmxkrnqrmslchvlarghbnqgdtyfrwsuhhodymsrpxgqptjlvhmlcazvvybuljbpaqqqqdcufkqgcknrlrwzbdtqqykdwrqputjxortexovmtpmeyogxxcykxpbknbrjvwgfdrjmrwxutbwzcialjnbokhddaonxfoqaxarkzslcwqorlhdpsbryswboxftjjbmvlvstzfgmvvltbziyflrddkyxslifvcunyxrmbhadolsebrumwcjlkzfpncweynspxpftcbahdwjlmaxyvigxubjgoimyqtxqiajidfmajgpkqpcznuafehnkznydfxuvfucngrxksggapliibymejxzcmbdrfbzdjxyzblphmkhqluqtviuzixhgwqqueeckurttbsssykhsexmqqtfeicpjckvsgrmcwayjpshkltnqapjbbhhihlalzeuddrmodkeofemhzgqwiyoygpajbqpscuzpzsprkyobbtypegbqbnodpiuwptxgvmizxcgcocqymcranquqnwggwjbcskwjvvnpfmhaohrhuzmfgskufilqstxinwdockopciyuaaeoqdappvlfzklqlpjrkaeigtlfvjcfuxlazrxnqupcnlkyqwfkyhpvnirltoxrckanedkezyekbiolscaqltwxpoybxrspmamjmdmjfflxeokelpsavsdvhqqbwtopsfkijdzsygkoinqwhufwnbgauiprsitlapkllaipwbdbzettoxmfddynxhrujwcouxgtrjemrxmceaatfxomyqyqjpiwducxpuyailvgiuxrzoonydokcymdgqzbuanzdxufcftqremdcrbyspoylvcqvyoyxhsbvlpamysyqltiwnsicvatgmztrmicpsedldlhylellpmqvhymryfhkbkdytdqlonsuzyqsimlsfxbdffpcziviwxfiraaoepadarqpldxecydtcogbpnuugbendyvxgpybhqzwgussybomxzdmmrvysqimxxyjqrvjwjjivwywdqmsgkgdzhpaahpanxkzqbhtjqdgjcybnufpwutuafdzegslokejhfwrrdmlyitegckpzyipmyhsdpukrgbduoifxqikvlahjkicjhtofiufnjdanzhtomtxswwcljezreipjlpkzmpkisklxanpdzzetfzecdjinacsuilnejspdqihzlbshvqfnycfwgcgzbmmpiwrwtrpnmkiegdahhttlqvxqbnqpbqyxkaslgxvwsyjyuahenadpmfinwdzcudgkjfwkahjs"
s12 = "deasvrgsdxhdbemwpenmbhjbnykuygxvmfkjagxnjoywjdgmjewtofmbpfehbfgauiihajsdbarllcmoqkqvebwvtitjqscqnantzpqtifwvmzlnkyuxoruhqlvvoqqdwzccprqmsrllrzfyvqgiyrbqlmskrqjdfdvygtsmijcqdhmpuqhrmsrwzsnnxpynjtechsxvlwhurtqbieshuragietmcokwxrlvehihspodjkkpweqekrjemnsimexuktmoqiowiyifqjsylmmejuhltwjfqfyyujuwdivyzctvrkefdzpwqrzpembtrcamzubewkanmgnmfjyatgnkxtmimnqsodgvnbkowvjebslcfdrqjkpjhfqojwtdfunhctckgipwgmtlzialllhcnarbbrtxgzddmryuohmjtsnpkkpvtipqjkucuqnqgdvvsquedghikbayosxjfwrvlnjpukbxhzruatdiwemwjnjpkwancvdniwiefcstdgyhycntmgroneylurnehnhjqjqomcgcwprwdoejlvaponqhyaultpxqvykydofkpurzqhygxmieyjotxhiqtvlnmffxurxhmrhvdkkgwaekojxocoofvznjynlzhbojbkljzhihfepmhuirqxsxjslbaoilykltzpqzjzvoqenjuayqmktpsoedxnwwibotpjgpmpfsnbipuammzlaogvekhzftqxrbmiwuhynpaznoqsxfiuacwogolvqvzbqlmunaemsvhlmtkavbzvhdignnhdziydpqaizjlytqjrhgtbdaxmgepysvtnampnldgpgtrbhtzhfbvclwustztaerkzggiekheckfquleawilaexocaggnxeygovsfzkjkeizfkfcffdrgzcftjlaluooqkgceoahlhwvfmwwkgqiqxstlzahtyzicnyboeqstdskkidqcseyrjfsucvyefbkikfjzesdpoxkhstiapcidwxaantpxzjxuipkzcrybgftemljmdaeisvfrnlrzlbbxukiggchmpriytsdqlzbjsgrfffwiwdupgjkudtemkncffcxxdeqepqcbmcfurwbjhsyvjxlzittwsodkgnfsklbzdclcsireusuzfraqmjrhbtyrnogsfllnjbxwicpsshhgiqgdnlvzybzdkgpngyylznhxaktgmiriqrfsigowybnrdfhwbknjpwqwrvcmvxpfqpburfglokymmwjshsjrdzlcxzmpwefyqwgjvvjlejhpcfvdfnlbyuvwdsoihailxypsoswpfauxdbaqukclmqikmimiryeptmygvkvmcjkkswthokvksoibotyrsprajrjucvukekiuyjnydiwaqpelrxadrhruhqoxhowbabtfwaxlvqbzpghijvbkxqqgmdksecjymvtrqqgycvmqjbdypphvfkhrfbnkxyyxkguxpdjvndwpihdtlvarfxveltnvmmdufihhqttmbpoyzwhieoblwjaoxbhmvmbklpuprlvqthmdskyixgcspiawdeoopxhzpsdtxsfjzrkdvnbtmbehjqowgtqdokaxwlqdhfvyxnaflcxinzmwptndasfclnrucjvixufbcdrwcxbjmvwmjzjcqnhgddugkaqqirmthedbfidisueqruimmvetezyzjvyqzucdlrlfaqldmtsrluhphqrwejqbcgafhqxfxceibvshmvdjubdinoeqlitgnhvjvbqwcvdhncxognwoaeyojayyrzmokpxsihhkzbkvaczlmepzhlwnyzdzborlwbhicmduieiwarxwpzgukknkplhmkcioficttdsbesbkysnpwhhqmpdctfqyawxxbrjmgbefhuajwedaingmrwfdptobbkfxgupczsahmxngmupbolysndbgswzlxldjynxrooiszcfyhixupcgudalteszwwkrhipqmxckzxydftkoxsmemggcxhizgqihcjnbnjaduhucwoxarpachkqmnhafddyhaoqkeskodukkgnnejjskykgwfnoyspcjgvnbjmxdnpvxjbwqkokzchcvddbuzgtbackxevisusequrqwrsmeqbffcfzzzdqvreeydfygkmkzftzgbkjznqqdpzanpojqhrrghmnmmjsgxnozjnieuffbsvtxzizwhhtcrszyjwlmbxklakzhymzvpuuywpqksauifkshzsdsnsgdbpmgvinihwykzzpoojukgltdcvncerrmxkrnqrmslchvlarghbnqgdtyfrwsuhhodymsrpxgqptjlvhmlcazvvybuljbpaqqqqdculkqgckdrlrwzbdtqqykdwrqputjxortexovmtpmeyogxxcykxpbknbrjvwgfdrjmrwxutbwzcijnjnbokhddaonxfoqaxarkzslcwqorlhdvsbryswboxftjjbmvlvstzfgmvvltbziyflrddkyxslifvcunyxrmbradolsebrumwcjlkzfpncweynspxpftcbahdwjlmaxyvigxubjgoimyqtxqiajidfmajgpkqpcznuafetnkznydfxuvfucngrxksggapliibymejxzcmbdrfbzdjxyzblphmkhqlubtviuzixhgwqqueeckurttbsssykhsexmqqtfeicpjckvsgrbcwayjpshkltnqapjbbhhinlalzeuddrmodkeofemhzgqweyoygpajbqpscuzpzsprkyobbtypegbqbnodpiuwptxgvmizxcgcocqymcranquqnwggwjbcskwjvvnpfmhaohhhuzmfgskufilqstxinwdockopciyuaaeoqdappvlfzklqlpjrkaeigdlfvjcfuxlazrxnqupcnlkyqwfkyhpvnirltoxrckanedkezyekbiolscaqltwxpoybxrspmamjmdmafflxeokelpsavsdvhqqbwtopsfkijdzsygkoihqwhyfwnbgauiprsitlapkllaipwbdbzettoxmfddynxhrujwcouxgtrjemrxmciaatfxomyqyqjpiwducepuyailvgiuxrzoonydokcymdgqzbuanzdxufcftqremdcrbyspoylvcqvyoyxhsbvlpamysyqltiwnsicvatgmztrmicpsedldlhylellpmqvhymryfhkbkdytdqlonsuzyqsimlsfxbdffpcziviwxfiraaoepadarqpldxecydtcogbpnuugbendyvxgpybhqzwgussybomxzdmmrvysqimxxyjqrpjwjjivwywdqmsgkgdzhpaahpalxkzqbhtjqdgjcybnufpwutuafdzegslokejhfwrrdmlyitegckpzyipmyhsdpukrgbduoiixqikvlahjkicjutofiufnjdanzhtomtxswwcljezreipjlpkzmpkisklxanidzzetfzecljinacsuilnejspdqihzlbshvqfnycfwgcgzbmmpiwrwtrpnmkiegdchhttlqvxqbnqpbqyxkaslgxvwsyjyuahenadpmfinwdzcudgkjfwkahjsyerluvhlmudkshnvhqygjxpfvblelciwbkiflnutrihyffamtmtnklexvvelsoyjypppvflbeoxorlfmhryxcvyeypxdtailsnfiuqapwhrovfrhkeqpzeysxhqyjpihbdnqpshyemgpxcnscfzgydmemuffryevsjxdcbynebxnhvfwpnhmmxzubjkmqkecmoqtugbxdwowcawjmqlmwjlwmaxftpdnprgxekkusmzuythqmqtacbyepvoickldankkssjyfpxqmabqorvtpgztuqyjgqjhmzmqnuyrfgjkrgoimnbhkzhoefscczbejgkjtztwwcsmalbezdtxihbyimigmotxuftbszrnquyvuxacdrwnzmstkxujwjcmmqmbennupqzvjgxgyrbttudkpprljznpjhadlavgzisehircbdnxmltfsmbffppszjtekdfeagpquf"

assert sol.checkInclusion(s1=s11, s2=s12) is True
