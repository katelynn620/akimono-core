# ���꒲�� 2005/01/06 �R��

DataRead();
CheckUserPass(1);

$disp.="<BIG>�����X�ʂ�F����\\��</BIG><br><br>";

# ���v/�����o�����X�v�Z
GetMarketStatus();

#�X�ʒǉ��o�[�W����
my $itemlist="";
$itemlist="<select name=itn>";
foreach($ITEM[0],grep(!$tp || $_->{type}==$tp,sort{$a->{sort} <=> $b->{sort}}values(%marketitemlist)))
{
	$itemlist.="<option value=\"$_->{no}\"".($_->{no}==$itn?' SELECTED':'').">".$_->{name};
}
$itemlist.="</select>";

my $shoplist="";
$shoplist="<select name=ds><option value=\"\">���ׂ�";
foreach (@DT)
{
	$shoplist.="<OPTION VALUE=\"$_->{id}\"".($Q{senditem}==$_->{id}?' SELECTED':'').">$_->{shopname}" if $DT->{id}!=$_->{id};
}
	$shoplist.="</select>";

$disp.=<<"HTML";
$TBT$TRT
<td valign="bottom">
<form action="action.cgi" $METHOD>
<input type=hidden name=key value="shop-a">
$USERPASSFORM
<input type=hidden name=tp value=\"$tp\">
$itemlist
<input type=submit value="���i�Ō���"> 
</form>
<td valign="bottom">
<form action="action.cgi" $METHOD>
<input type=hidden name=key value="shop-b">
$USERPASSFORM
$shoplist
<input type=submit value="�X���Ō���"> 
</form>
<td valign="bottom">
<form action="action.cgi" $METHOD>
<input type=hidden name=key value="shop-c">
$USERPASSFORM
<input type=submit value="����𒲍�">
</form>
$TRE$TBE
<br>
HTML

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar(keys(%marketitemlist)));

$disp.=GetPageControl($pageprev,$pagenext,"t=3","",$pagemax,$page);

$disp.=$TB;
$disp.=$TR;
$disp.=$TDB.'���i��';
$disp.=$TDB.'����<small>/�O��</small><br>�����㐔';
$disp.=$TDB.'�ň��l';
$disp.=$TDB.'�ō��l';
$disp.=$TDB.'�̔�����';
$disp.=$TDB.'�W�����i';
$disp.=$TDB.'���v�����o�����X';
$disp.=$TRE;
foreach my $ITEM ((sort{$a->{sort} <=> $b->{sort}} values(%marketitemlist))[$pagestart..$pageend])
{
	my $itemno=$ITEM->{no};
	$disp.=$TR;
	$disp.=$TDNW."<A HREF='action.cgi?key=shop-a&$USERPASSURL&itn=".$itemno."'>";
	$disp.=GetTagImgItemType($itemno).$ITEM->{name}."</A>";
	$disp.=$TDNW.$ITEM->{todaysale}."<small>/".$ITEM->{yesterdaysale}."</small>";
	$disp.=$TDNW.($ITEM->{marketprice} ? GetMoneyString($ITEM->{marketpricelow}) : ($MOBILE?'0':' '));
	$disp.=$TDNW.($ITEM->{marketprice} ? GetMoneyString($ITEM->{marketpricehigh}) : ($MOBILE?'0':' '));
	$disp.=$TDNW.($ITEM->{marketprice} ? GetMoneyString($ITEM->{marketprice}) : ($MOBILE?'0':' '));
	$disp.=$TDNW.GetMoneyString($ITEM->{price});
	$disp.=$TDNW.GetMarketStatusGraph($ITEM->{uppoint});
	#$disp.=$TDNW.$todaystock{$itemno};
	$disp.=$TRE;
}
$disp.=$TBE;
$disp.=GetPageControl($pageprev,$pagenext,"t=3","",$pagemax,$page);

OutSkin();
1;
