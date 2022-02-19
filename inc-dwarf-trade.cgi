# �f�Օi���X�g�\�� 2005/01/06 �R��

OutError("bad request") unless -e "trade.cgi";
CheckTradeProcess();

$tp=int($Q{tp}+0);
@itemlist=();
%itemlist=();

my %itemcode2idx=();
%itemprice2idx=();
foreach(0..$MAX_ITEM){
$itemcode2idx{$ITEM[$_]->{code}}=$_;
$itemprice2idx{int($ITEM[$_]->{price}/100)}=$_ unless $ITEM[$_]->{flag}=~/r/;;
}

open(IN,GetPath("trade"));
($TRADE_STOCK_TIME)=split(/[\t\n]/,<IN>);
while(<IN>)
{
	chop;
	my($trademode,$tradetime,$tradecode,$shopinfo,$buycount)=split(/\t/);
	my($hostcode  ,$boxno  ,$itemcode,$itemcnt,$price)=split(/!/,$tradecode);
	my($hostcode_s,$boxno_s,$shopinfo_s)=split(/!/,$shopinfo,3);
	my($shopname,$hostname,$msg)        =split(/,/,$shopinfo_s);
	my $itemno=$itemcode2idx{$itemcode};
	my $data="$hostcode!$boxno";
	
	$itemno=ConvertItem(int($price/$itemcnt)),$data.="!$itemcode" if (!$itemno || $ITEM[$itemno]->{flag}=~/r/);
	next if $itemno==-1;
	next if $tp!=0 && $ITEM[$itemno]->{type}!=$tp;
	$itemlist{$itemno}=1;
	push(@itemlist,[$tradecode,$shopname,$hostname,$itemno,$itemcnt,$price,$msg,$tradetime,$buycount,$data]) if (!$Q{itn} || $Q{itn}==$itemno);
}
close(IN);

@itemlist=sort { $a->[7] <=> $b->[7] } @itemlist;

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$RANKING_PAGE_ROWS,scalar(@itemlist));

$disp.=GetMenuTag('dwarf','[��z�փ��X�g]')
	.GetMenuTag('dwarf',		'[��z�ւ��o��]','&form=make');
$disp.=GetMenuTag('dwarf','[�f�Օi���X�g]','&trade=list') if -e "trade.cgi";
$disp.="<hr width=500 noshade size=1>";

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�Z�ݍ��݃h���[�t</SPAN>�F���܎�舵�����̖f�Օi�͎��̒ʂ肶��B<br>
�~���������������炷���Ɏ葱����Ƃ悢�̂��B
$TRE$TBE<br>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="trade">
<BIG>�����`���̖f�Օi</BIG><br><br>
HTML

foreach my $cnt (0..$#ITEMTYPE)
{
	$disp.=$cnt==$tp ? "[" : "<A HREF=\"action.cgi?key=dwarf&$USERPASSURL&trade=list&tp=$cnt\">";
	$disp.=GetTagImgItemType(0,$cnt) if $cnt && !$MOBILE;
	$disp.=$ITEMTYPE[$cnt];
	$disp.=$cnt==$tp ? "]" :"</A>";
	$disp.=" ";
}
	$disp.="<br>";

$pagectrl=GetPageControl($pageprev,$pagenext,"trade=list&tp=$tp","",$pagemax,$page);
$disp.=$pagectrl;
$disp.=$TB;

	$disp.=<<"HTML";
$TB$TR
$TD�^
$TDB���t�i
$TDB���
$TDB���t��
$TDB���
$TDB����
$TRE
HTML

my @MODE;
$MODE[1]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign1.png">�̔���|;
$MODE[2]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign2.png">����ς�|;

my $allbuy=1;
foreach my $cnt ($pagestart .. $pageend)
{
	my $item=$itemlist[$cnt];
	my $lasttime=$TRADE_STOCK_TIME-$NOW_TIME+$item->[7];
	$disp.=$TR.$TDNW;
	$disp.="<input type=radio name=\"code\" value=\"$item->[9]:$item->[3]:$item->[4]:$item->[5]\">",$allbuy=0 if !$item->[8];
	$disp.=$TD;
	$disp.=GetTagImgItemType($item->[3]).$ITEM[$item->[3]]->{name}.' '.$item->[4].$ITEM[$item->[3]]->{scale};
	$disp.='<br><small>(�艿 '.GetMoneyString($ITEM[$item->[3]]->{price} * $item->[4]).')</small>';
	
	$disp.=$TDNW.GetMoneyString($item->[5]);
	$disp.=$TDNW.$item->[1]."<br><small> (".$item->[2].")</small>";
	$disp.=$TDNW;
	$disp.=($item->[8] ? $MODE[2] : $MODE[1]);
	$disp.=$TD.($lasttime>0 ? "����".GetTime2HMS($lasttime) : "�܂��Ȃ�");
	$disp.=$TRE;
}
$disp.=$TBE."<br>";
$disp.=<<"HTML" if !$allbuy;
�I�������f�Օi�ɂ��� <INPUT TYPE=SUBMIT VALUE="�A����\\������">
</FORM>
HTML

1;


sub CheckTradeProcess
{
	my $fn=GetPath($TRADE_LOCK_FILE);
	return if !-e $fn;
	
	if((stat($fn))[9]<$NOW_TIME-60*30)
	{
		#30���ȏ�̃��b�N�ُ͈�ƌ��Ȃ�����
		Lock();
		unlink($fn) if (stat($fn))[9]<$NOW_TIME-60*30; #���ɉ�������Ă���\�����`�F�b�N�����
		UnLock();
	}
	OutError('�������f�ՑD�����`���Ă��܂��B�������΂炭���҂���������');
}

sub ConvertItem
{
	my ($price)=@_;
	my $no=int($price/100);
	my $itemno=$itemprice2idx{$no};
	return $itemno if $itemno;
	foreach(1..12)
		{
		$tno=$no + $_;
		$itemno=$itemprice2idx{$tno};
		return $itemno if $itemno;
		next if $no <= $_;
		my $tno=$no - $_;
		$itemno=$itemprice2idx{$tno};
		return $itemno if $itemno;
		}
	return -1;
}

