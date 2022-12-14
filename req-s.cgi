use utf8;
# 依頼処理 2005/03/30 由來

Lock();
DataRead();
CheckUserPass();
RequireFile('inc-req.cgi');

$disp.="<BIG>●".l('依頼所')."</BIG><br><br>";

my $functionname=$Q{mode};
OutError('bad request') if !defined(&$functionname);
&$functionname;

$disp.="<br><br>".$TBT.$TRT.$TD.GetTagImgJob($DT->{job},$DT->{icon});
$disp.=$TD.GetMenuTag('stock',	'['.l('倉庫へ').']');
$disp.=GetMenuTag('req','['.l('続けて依頼を見る').']');
$disp.=$TRE.$TBE;

WriteAuc();
DataWrite();
DataCommitOrAbort();
UnLock();
OutSkin();
1;


sub new
{
	my ($numrate,$prrate);
	$itemno=$Q{it};
	$num=CheckCount($Q{num},0,0,$MAX_MONEY);
	$prn=$Q{prn};
	$pr=CheckCount($Q{pr},0,0,$MAX_MONEY);
	$pr=$pr * $num if ($Q{unit})&&($prn < 0);
	$num=$num * $pr if ($Q{unit})&&($itemno < 0);
	OutError($AucImg.l('依頼品の個数や価格の指定を忘れてるみたいだぜ。')) if ($pr < 1) ;
	OutError($AucImg.l('報酬品の個数や価格の指定を忘れてるみたいだぜ。')) if ($num < 1) ;
	if ($itemno > 0) {
		OutError($AucImg.l('おいおい，ない袖は振れないぜ！')) if ($DT->{item}[$itemno-1] < $num) ;
		OutError($AucImg.l('その品物を出品することはできないぜ。')) if ($ITEM[$itemno]->{flag}=~/r/) ;	# r 依頼不可
		$numrate=$ITEM[$itemno]->{price} * $num;
		} else {
		OutError($AucImg.l('おいおい，ない袖は振れないぜ！')) if ($DT->{money} < $num);
		$numrate=$num;
		}
	OutError($AucImg.l('依頼品と報酬品が同じじゃあ取引にならないぜ！')) if ($itemno == $prn) ;
	if ($prn > 0) {
		OutError($AucImg.l('依頼品の個数が多すぎて達成できそうもないぜ。')) if ($pr > $ITEM[$prn]->{limit}) ;
		OutError($AucImg.l('その品物を依頼することはできないぜ。')) if ($ITEM[$prn]->{flag}=~/r/)||($ITEM[$prn]->{flag}=~/o/);	# o 出品のみ
		$prrate=$ITEM[$prn]->{price} * $pr;
		} else {
		$prrate=$pr;
		}
	OutError($AucImg.l('依頼と報酬の価値がつりあっていないぜ。条件を見直してくれ。')) if ($prrate > $numrate * 2) || ($numrate > $prrate * 2);

	my @list=map{$_->{id}}@REQ;
	@list=grep($_ eq $DT->{id},@list);
	OutError($AucImg.l('これ以上依頼を出すことはできないぜ！')) if (scalar(@list) >= $REQUEST_CAPACITY);

	@REQ=reverse(@REQ);
	$Scount++;
	my $i=$Scount;
	$REQ[$i]->{no}=($i > 0) ? ($REQ[$i-1]->{no} + 1) : 1;
	$REQ[$i]->{id}=$Q{id};
	$REQ[$i]->{mode}=0;
	$REQ[$i]->{tm}=$NOW_TIME + $REQUEST_LIMIT;
	($REQ[$i]->{itemno},$REQ[$i]->{num},$REQ[$i]->{prn},$REQ[$i]->{pr})=($itemno,$num,$prn,$pr);
	@REQ=reverse(@REQ);

	$DT->{item}[$itemno-1]-=$num if ($itemno > 0);
	$DT->{money}-=$num , $DT->{paytoday}+=$num if ($itemno < 0);

	my $cost=0;
	$cost=int($num * $DTTaxrate / 100) if ($itemno < 0);
	$cost=int($pr * $DTTaxrate / 100) if ($prn < 0);
	OutError($AucImg.l('おや，資金が足りなくて税金を払えないみたいだぜ。')) if ($cost > $DT->{money});
	$DT->{taxtoday}+=$cost;
	$DT->{money}-=$cost;
	$disp.=$AucImg.l('依頼を作成したぜ。早く達成されるといいな！');
}

sub plus
{
	$i=SearchReqIndex($Q{idx});
	OutError(l('指定された取引は存在しません')) if ($i==-1);
	my($itemno,$num,$prn,$pr,$mode)=($REQ[$i]->{itemno},$REQ[$i]->{num},$REQ[$i]->{prn},$REQ[$i]->{pr},$REQ[$i]->{mode});
	OutError($AucImg.l('この取引はもう達成されてるぜ。またよろしく頼むな。')) if defined($id2idx{$mode});
	OutError($AucImg.l('おいおい、ない袖は振れないぜ！')) if ($prn > 0)&&($DT->{item}[$prn-1] < $pr) ;
	OutError($AucImg.l('おいおい、ない袖は振れないぜ！')) if ($prn < 0)&&($DT->{money} < $pr) ;

	$DT->{item}[$prn-1]-=$pr if ($prn > 0);
	$DT->{money}-=$pr, $DT->{paytoday}+=$pr if ($prn < 0);

	if ($itemno > 0)
		{
		$DT->{item}[$itemno-1]+=$num;
		$DT->{item}[$itemno-1]=$ITEM[$itemno]->{limit} if ($DT->{item}[$itemno-1]>$ITEM[$itemno]->{limit});
		$disp.=$AucImg.l('これが報酬の%1 %2だ。ごくろうさん！',$ITEM[$itemno]->{name},$num.$ITEM[$itemno]->{scale});
		}
	else
		{
		$DT->{money}+=$num;
		$DT->{saletoday}+=$num;
		$DT[$id2idx{$id}]->{paytoday}+=$pr if defined($id2idx{$id});
		$disp.=$AucImg.l('これが報酬の%1だ。ごくろうさん！',GetMoneyString($num));
		}
	$REQ[$i]->{mode}=$DT->{id};
}

sub end
{
	$i=SearchReqIndex($Q{idx});
	OutError(l('指定された取引は存在しません')) if ($i==-1);
	my($itemno,$num)=($REQ[$i]->{itemno},$REQ[$i]->{num});

	if ($itemno> 0)
		{
		$DT->{item}[$itemno-1]+=$num;
		$DT->{item}[$itemno-1]=$ITEM[$itemno]->{limit} if ($DT->{item}[$itemno-1]>$ITEM[$itemno]->{limit});
		}
		else
		{
	$DT->{money}+=$num;
		}

	undef $REQ[$i];
	$disp.=$AucImg.l('今回の依頼を打ち切ったぜ。またよろしく頼むな。');
}

sub thank
{
	$i=SearchReqIndex($Q{idx});
	OutError(l('指定された取引は存在しません')) if ($i==-1);
	OutError(l('不正な要求です')) if ($REQ[$i]->{id} != $DT->{id});
	my($no,$itemno,$num,$prn,$pr,$mode)=($REQ[$i]->{no},$REQ[$i]->{itemno},$REQ[$i]->{num},$REQ[$i]->{prn},$REQ[$i]->{pr},$REQ[$i]->{mode});

	if ($prn > 0) {
		$DT->{item}[$prn-1]+=$pr;
		$DT->{item}[$prn-1]=$ITEM[$prn]->{limit} if ($DT->{item}[$prn-1]>$ITEM[$prn]->{limit});
		$disp.=$AucImg.l('これが依頼品の%1 %2%3だ。',$ITEM[$prn]->{name},$pr,$ITEM[$prn]->{scale}).'<br>';
		$disp.=l('%1さんが届けてくれたぜ！',$DT[$id2idx{$mode}]->{shopname});
		}
		else
		{
		$DT->{money}+=$pr;
		$DT->{saletoday}+=$pr;
		$disp.=$AucImg.l('これが代金の%1だ。',GetMoneyString($pr)).'<br>';
		$disp.=l('%1さんが払ってくれたぜ！',$DT[$id2idx{$mode}]->{shopname});
		}
	undef $REQ[$i];
}

sub WriteAuc
{
	my @buf;
	foreach my $i(0..$Scount)
		{
		next unless defined($REQ[$i]->{no});
		$buf[$i]=join(",",map{$REQ[$i]->{$_}}@REQnamelist)."\n";
		}
	OpenAndCheck(GetPath($TEMP_DIR,"request"));
	print OUT @buf;
	close(OUT);
}

