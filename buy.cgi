# �d����ڍ� 2005/01/06 �R��

$NOMENU=1;
DataRead();
CheckUserPass();

($id,$showcase,$mstno)=split('!',$Q{buy},3);
$id=int($id+0);
$showcase=int($showcase+0);

if($id==0)
{
	# �s��
	$DTS=GetWholeStore();
}
else
{
	# ��ʓX
	$DTS=$DT[(CheckUserID($id))[1]];
}

$showcase=CheckShowCaseNumber($DTS,$showcase);
($itemno,$price,$stock)=CheckShowCaseItem($DTS,$showcase);

OutError("��I�ɂ͉�������܂���") if !$itemno || !$stock;
OutError("�񂪕ω������悤�ł�") if $itemno!=$mstno;

RequireFile('inc-html-ownerinfo.cgi');

$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if !$id;
my $usetime=GetTimeDeal($price,$itemno,1);

my $baseprice=$price;
my($guild,$guildrate,$guildmargin)=CheckGuild($DT,$DTS,$baseprice);
my $saleprice=$baseprice+($guild==1 ? -$guildmargin : $guildmargin);
$price=$saleprice;

$disp.="<BIG>���w��</BIG><br><br>";

my $ITEM=$ITEM[$itemno];

$disp.=$TB.$TR.$TDB."�X��".$TD.GetTagImgGuild($DTS->{guild}).$DTS->{shopname}.$TRE;
$disp.=$TR.$TDB;
$disp.=(($ITEM->{flag}=~/h/)? "���O" : "���i");
$disp.=$TD.GetTagImgItemType($itemno).$ITEM->{name}.$TRE;
$disp.=$TR.$TDB.$TD.$ITEM->{info}.$TRE;
$disp.=$TR.$TDB."���i".$TD.'@'.GetMoneyString($baseprice).$TRE;
$disp.=$TR.$TDB.("�M���h���������i","�M���h�Ԋ������i")[$guild-1].$TD.'@'.GetMoneyString($saleprice).$TRE if $guild>0;
$disp.=$TR.$TDB."�M���h�����s��".$TD."�M���h�������⏕�͂���܂���".$TRE if $guild==-1;
$disp.=$TR.$TDB."�̔��݌ɐ�".$TD.$stock.$ITEM->{scale}.$TRE;
$disp.=$TR.$TDB.'���X�ۗL��'.$TD.($DT->{item}[$itemno-1]+0).$ITEM->{scale}.$TRE;
$disp.=$TBE;

if ($ITEM->{flag}!~/s/) {		# s ��s��
	$disp.="<SPAN>�����̏��i�͒񂵂Ă�����܂���</SPAN><br>" if ($ITEM->{popular}==0);
	$disp.="<SPAN>�����̏��i�͒񂵂Ă��قƂ�ǔ���܂���</SPAN><br>" if ($ITEM->{popular} > 800000);
	}
$disp.="<hr width=500 noshade size=1>";

if($DT->{item}[$itemno-1]>=$ITEM->{limit})
	{$disp.='<BR>�����q�ɂ�'.$ITEM->{name}.'����t�ł�<BR>';}
elsif($DT->{money}<$price && $price > 0)
	{$disp.='<BR>����������܂���<BR>';}
elsif(GetStockTime($DT->{time})<$usetime)
	{$disp.='<BR>���Ԃ�����܂���<BR>';}
else
{
	$disp.="<FORM ACTION=\"action.cgi\" $METHOD>";
	$disp.="<INPUT TYPE=HIDDEN NAME=key VALUE=\"buy-s\">";
	$disp.="$USERPASSFORM";
	$disp.="<INPUT TYPE=HIDDEN NAME=bk VALUE=\"$Q{bk}\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=id VALUE=\"$id\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=pr VALUE=\"$price\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=sc VALUE=\"$showcase\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=it VALUE=\"$itemno\">";
	$disp.="��L�� ";
	$limit=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1];
	my $money=$MAX_MONEY;
	$money=int($DT->{money}/$price) if $price;
	$msg{1}=1;
	$msg{10}=10;
	$msg{100}=100;
	$msg{1000}=1000;
	$msg{10000}=10000;
	$msg{$stock}="$stock(�S��)";
	$msg{$limit}="$limit(�q�ɍő�)";
	$msg{$money}="$money(�����ő�)";
	$disp.="<SELECT NAME=num1 SIZE=1>";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1,10,100,1000,10000,$stock,$limit,$money))
	{
		last if $stock<$cnt || $cnt>$money || $cnt>$limit || $cnt==$oldcnt;
	
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.="</SELECT> $ITEM[$itemno]->{scale}�A�������� ";
	$disp.="<INPUT TYPE=TEXT NAME=num2 SIZE=5> $ITEM[$itemno]->{scale} ";

  if ($ITEM->{flag}=~/h/) {  $disp.="<INPUT TYPE=SUBMIT VALUE='�ق�'>";  }
         else 	{ $disp.="<INPUT TYPE=SUBMIT VALUE='����'>"; }

	$disp.="<br>(�����:".GetTime2HMS($usetime).")";
	$disp.="</FORM>";
}

OutSkin();
1;
