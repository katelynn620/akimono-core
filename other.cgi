use utf8;
# 各種手続 2005/01/06 由來

DataRead();
CheckUserPass();
RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>●".l('各種手続')."</BIG><br><br>";

$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=comment>
$USERPASSFORM
<SPAN>${\l('コメント')}</SPAN>
<INPUT TYPE=TEXT NAME=cmt SIZE=36 VALUE="$DT->{comment}">
<INPUT TYPE=SUBMIT VALUE="${\l('変更する')}">
</FORM>
STR

$i_rand=int(rand($ICON_NUMBER))+1;
$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=icon>
$USERPASSFORM
<SPAN>${\l('店長アイコン変更')}</SPAN>：
<input type="button" value="${\l('アイコン一覧')}" onclick="javascript:window.open('action.cgi?key=icon','_blank','width=450,height=380,scrollbars')">
<SELECT NAME=icon>
<OPTION value="$i_rand" selected>${\l('ランダム')}</OPTION>
STR

foreach my $i(1..$ICON_NUMBER)
	{
	$disp.="<OPTION value=\"$i\">".l('画像')."$i</OPTION>";
	}

$disp.=<<"STR";
</SELECT> 
<INPUT TYPE=SUBMIT VALUE="${\l('変更する')}">
</FORM>
STR

$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=shopname>
$USERPASSFORM
<SPAN>${\l('店舗名変更')}</SPAN>(${\l('改名費用')}$term[0]50,000$term[1])
<INPUT TYPE=TEXT NAME=rename SIZE=30 VALUE="">
<INPUT TYPE=SUBMIT VALUE="${\l('改名する')}">
</FORM>
STR

$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=owname>
$USERPASSFORM
<SPAN>${\l('店長名変更')}</SPAN>(${\l('改名費用')}$term[0]50,000$term[1])
<INPUT TYPE=TEXT NAME=owname SIZE=20 VALUE="">
<INPUT TYPE=SUBMIT VALUE="${\l('改名する')}">
</FORM>
STR

$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=repass>
$USERPASSFORM
<SPAN>${\l('パスワード変更')}</SPAN> ： 
<INPUT TYPE=TEXT NAME=pw1 SIZE=10 maxlength=12 VALUE="">${\l('新パス ')}
<INPUT TYPE=TEXT NAME=pw2 SIZE=10 maxlength=12 VALUE="">${\l('新パス再入力')} 
<INPUT TYPE=SUBMIT VALUE="${\l('変更する')}">
</FORM>
STR


if ( ($NOW_TIME-$DT->{foundation}) > 3600*3 ) {
$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=restart>
$USERPASSFORM
<BIG>●${\l('再出発(やり直し)')}</BIG> ： 
<INPUT TYPE=TEXT NAME=rss SIZE=10 maxlength=12 VALUE="">${\l('確認のため restart と入力')}
<INPUT TYPE=SUBMIT VALUE="${\l('やり直す')}">
</FORM>
STR
} else {
$disp.=<<STR;
<hr width=500 noshade size=1>
<BIG>●${\l('再出発(やり直し)')}</BIG> ： 
<b>${\l('創業後3時間以内は再出発できません')}</b>
STR
}

$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=cls>
$USERPASSFORM
<BIG>●${\l('閉店(再登録不可)')}</BIG> ： 
<INPUT TYPE=TEXT NAME=cls SIZE=10 maxlength=12 VALUE="">${\l('確認のため closeshop と入力')}
<INPUT TYPE=SUBMIT VALUE="${\l('店じまい')}">
</FORM>
STR

OutSkin();
1;
