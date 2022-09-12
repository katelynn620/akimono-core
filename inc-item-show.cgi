use utf8;
# アイテム陳列下請け 2004/01/20 由來

$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="sc-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=bk VALUE="$Q{bk}">
<INPUT TYPE=HIDDEN NAME=item VALUE="$itemno">
<BIG>●${\l('陳列')}：</BIG>
<SELECT NAME=no>
STR
foreach my $cnt (1..$DT->{showcasecount})
{
	$disp.="<OPTION VALUE='".($cnt-1)."'".($showcase==$cnt?' SELECTED':'').">";
	$disp.=l("棚%1",$cnt)."($ITEM[$DT->{showcase}[$cnt-1]]->{name})";
}
	$disp.="</SELECT>";
	$disp.=l("へ標準価格の");
	$disp.=<<STR;
<SELECT NAME=per>
<OPTION VALUE='50'>${\l('5割引')}
<OPTION VALUE='60'>${\l('4割引')}
<OPTION VALUE='70'>${\l('3割引')}
<OPTION VALUE='80'>${\l('2割引')}
<OPTION VALUE='90'>${\l('1割引')}
<OPTION VALUE='100' SELECTED>${\l('まま')}
<OPTION VALUE='110'>${\l('1割増')}
<OPTION VALUE='120'>${\l('2割増')}
</SELECT>
${\l('または')}
<INPUT TYPE=TEXT NAME=prc SIZE=6 VALUE="$Q{pr}">
${\l('%1で',$term[2])}
<INPUT TYPE=SUBMIT VALUE='${\l('陳列する')}'>
(${\l('時間%1消費',GetTime2HMS($TIME_EDIT_SHOWCASE))})
</FORM>
STR
1;
