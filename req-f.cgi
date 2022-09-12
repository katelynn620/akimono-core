use utf8;
# 依頼フォーム 2005/03/30 由來

DataRead();
CheckUserPass();
RequireFile('inc-req.cgi');
RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>●".l('依頼所')."</BIG><br><br>";

ReqSet();
my $limit=GetTime2HMS($REQUEST_LIMIT);
$disp.=<<STR;
$TB$TR$TD
$AucImg
${\l('新しい依頼書を書くんだな？ それなら注意事項をよく読んでくれ。')}<br>
・${\l('依頼は同時に <b>%1つ</b>しかすることができません。',$REQUEST_CAPACITY)}<br>
・${\l('依頼が達成されたら<SPAN>取りに来てください</SPAN>。')}<br>
・${\l('有効期限 <b> %1</b>以内に取りに来ないと依頼は破棄されます。',$limit)}<br>
・${\l('販売/買取では価格の <b>%1%</b>の税金が依頼者にかかります。',$DTTaxrate)}
$TRE$TBE
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="req-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="new">
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<BIG>●${\l('交換タイプ')}</BIG>：${\l('依頼品')} <SELECT NAME=prn SIZE=1>
$formlist
</SELECT> ${\l('を数量')} <INPUT TYPE=TEXT NAME=pr SIZE=7> ${\l('持って来てくれた方には')}<br>
お礼 <SELECT NAME=it SIZE=1>
$formitem
</SELECT> ${\l('を数量')} <INPUT TYPE=TEXT NAME=num SIZE=7> ${\l('差し上げます。')}
<INPUT TYPE=SUBMIT VALUE='${\l('作成')}'>
</FORM>
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="req-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="new">
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<BIG>●${\l('販売タイプ')}</BIG>：${\l('販売品')} <SELECT NAME=it SIZE=1>
$formitem
</SELECT> ${\l('を数量')} <INPUT TYPE=TEXT NAME=num SIZE=7> ${\l('売り出すので')}<br>
価格 <INPUT TYPE=TEXT NAME=pr SIZE=7> $term[2](
<INPUT TYPE=CHECKBOX NAME=unit>${\l('単価指定')})${\l('で買ってください。')}
<INPUT TYPE=HIDDEN NAME=prn VALUE="-1">
<INPUT TYPE=SUBMIT VALUE='${\l('作成')}'>
</FORM>
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="req-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="new">
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<BIG>●${\l('買取タイプ')}</BIG>：${\l('依頼品')} <SELECT NAME=prn SIZE=1>
$formlist
</SELECT> ${\l('を数量')} <INPUT TYPE=TEXT NAME=pr SIZE=7> ${\l('持って来てくれた方には')}<br>
価格 <INPUT TYPE=TEXT NAME=num SIZE=7> $term[2](
<INPUT TYPE=HIDDEN NAME=it VALUE="-1">
<INPUT TYPE=CHECKBOX NAME=unit>${\l('単価指定')})${\l('で買い取ります。')}
<INPUT TYPE=SUBMIT VALUE='${\l('作成')}'>
</FORM>
STR
OutSkin();
1;


sub ReqSet
{
	my @sort;
	foreach(1..$MAX_ITEM){$sort[$_]=$ITEM[$_]->{sort}};
	my @itemlist=sort { $sort[$a] <=> $sort[$b] } (1..$MAX_ITEM);
	$formitem="";
	$formlist="";		#全体のリスト
	foreach my $idx (@itemlist)
	{
		next if !$ITEM[$idx]->{name};
		next if $ITEM[$idx]->{flag}=~/r/;	# r 依頼不可
		my $cnt=$DT->{item}[$idx-1];
		my $scale=$ITEM[$idx]->{scale};
		my $price=$ITEM[$idx]->{price};
		$formlist.="<OPTION VALUE=\"$idx\">$ITEM[$idx]->{name}(@".GetMoneyString($price).")" if $ITEM[$idx]->{flag}!~/o/;		# o 依頼は出品のみ
		$formitem.="<OPTION VALUE=\"$idx\">$ITEM[$idx]->{name}($cnt$scale@".GetMoneyString($price).")" if $cnt;
	}
}

