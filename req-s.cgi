# �˗����� 2005/03/30 �R��

Lock();
DataRead();
CheckUserPass();
RequireFile('inc-req.cgi');

$disp.="<BIG>���˗���</BIG><br><br>";

my $functionname=$Q{mode};
OutError("bad request") if !defined(&$functionname);
&$functionname;

$disp.="<br><br>".$TBT.$TRT.$TD.GetTagImgJob($DT->{job},$DT->{icon});
$disp.=$TD.GetMenuTag('stock',	'[�q�ɂ�]');
$disp.=GetMenuTag('req','[�����Ĉ˗�������]');
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
	OutError($AucImg.'�˗��i�̌��≿�i�̎w���Y��Ă�݂��������B') if ($pr < 1) ;
	OutError($AucImg.'��V�i�̌��≿�i�̎w���Y��Ă�݂��������B') if ($num < 1) ;
	if ($itemno > 0) {
		OutError($AucImg.'���������C�Ȃ����͐U��Ȃ����I') if ($DT->{item}[$itemno-1] < $num) ;
		OutError($AucImg.'���̕i�����o�i���邱�Ƃ͂ł��Ȃ����B') if ($ITEM[$itemno]->{flag}=~/r/) ;	# r �˗��s��
		$numrate=$ITEM[$itemno]->{price} * $num;
		} else {
		OutError($AucImg.'���������C�Ȃ����͐U��Ȃ����I') if ($DT->{money} < $num);
		$numrate=$num;
		}
	OutError($AucImg.'�˗��i�ƕ�V�i���������Ⴀ����ɂȂ�Ȃ����I') if ($itemno == $prn) ;
	if ($prn > 0) {
		OutError($AucImg.'�˗��i�̌����������ĒB���ł��������Ȃ����B') if ($pr > $ITEM[$prn]->{limit}) ;
		OutError($AucImg.'���̕i�����˗����邱�Ƃ͂ł��Ȃ����B') if ($ITEM[$prn]->{flag}=~/r/)||($ITEM[$prn]->{flag}=~/o/);	# o �o�i�̂�
		$prrate=$ITEM[$prn]->{price} * $pr;
		} else {
		$prrate=$pr;
		}
	OutError($AucImg.'�˗��ƕ�V�̉��l���肠���Ă��Ȃ����B�������������Ă���B') if ($prrate > $numrate * 2) || ($numrate > $prrate * 2);

	my @list=map{$_->{id}}@REQ;
	@list=grep($_ eq $DT->{id},@list);
	OutError($AucImg.'����ȏ�˗����o�����Ƃ͂ł��Ȃ����I') if (scalar(@list) >= $REQUEST_CAPACITY);

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
	OutError($AucImg.'����C����������Ȃ��Đŋ��𕥂��Ȃ��݂��������B') if ($cost > $DT->{money});
	$DT->{taxtoday}+=$cost;
	$DT->{money}-=$cost;
	$disp.=$AucImg.'�˗����쐬�������B�����B�������Ƃ����ȁI';
}

sub plus
{
	$i=SearchReqIndex($Q{idx});
	OutError('�w�肳�ꂽ����͑��݂��܂���') if ($i==-1);
	my($itemno,$num,$prn,$pr,$mode)=($REQ[$i]->{itemno},$REQ[$i]->{num},$REQ[$i]->{prn},$REQ[$i]->{pr},$REQ[$i]->{mode});
	OutError($AucImg.'���̎���͂����B������Ă邺�B�܂���낵�����ނȁB') if defined($id2idx{$mode});
	OutError($AucImg.'���������A�Ȃ����͐U��Ȃ����I') if ($prn > 0)&&($DT->{item}[$prn-1] < $pr) ;
	OutError($AucImg.'���������A�Ȃ����͐U��Ȃ����I') if ($prn < 0)&&($DT->{money} < $pr) ;

	$DT->{item}[$prn-1]-=$pr if ($prn > 0);
	$DT->{money}-=$pr, $DT->{paytoday}+=$pr if ($prn < 0);

	if ($itemno > 0)
		{
		$DT->{item}[$itemno-1]+=$num;
		$DT->{item}[$itemno-1]=$ITEM[$itemno]->{limit} if ($DT->{item}[$itemno-1]>$ITEM[$itemno]->{limit});
		$disp.=$AucImg.'���ꂪ��V��'.$ITEM[$itemno]->{name}.' '.$num.$ITEM[$itemno]->{scale}.'���B�����낤����I';
		}
	else
		{
		$DT->{money}+=$num;
		$DT->{saletoday}+=$num;
		$DT[$id2idx{$id}]->{paytoday}+=$pr if defined($id2idx{$id});
		$disp.=$AucImg.'���ꂪ��V��'.GetMoneyString($num).'���B�����낤����I';
		}
	$REQ[$i]->{mode}=$DT->{id};
}

sub end
{
	$i=SearchReqIndex($Q{idx});
	OutError('�w�肳�ꂽ����͑��݂��܂���') if ($i==-1);
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
	$disp.=$AucImg.'����̈˗���ł��؂������B�܂���낵�����ނȁB';
}

sub thank
{
	$i=SearchReqIndex($Q{idx});
	OutError('�w�肳�ꂽ����͑��݂��܂���') if ($i==-1);
	OutError('�s���ȗv���ł�') if ($REQ[$i]->{id} != $DT->{id});
	my($no,$itemno,$num,$prn,$pr,$mode)=($REQ[$i]->{no},$REQ[$i]->{itemno},$REQ[$i]->{num},$REQ[$i]->{prn},$REQ[$i]->{pr},$REQ[$i]->{mode});

	if ($prn > 0) {
		$DT->{item}[$prn-1]+=$pr;
		$DT->{item}[$prn-1]=$ITEM[$prn]->{limit} if ($DT->{item}[$prn-1]>$ITEM[$prn]->{limit});
		$disp.=$AucImg.'���ꂪ�˗��i��'.$ITEM[$prn]->{name}.' '.$pr.$ITEM[$prn]->{scale}.'���B<br>';
		$disp.=$DT[$id2idx{$mode}]->{shopname}.'���񂪓͂��Ă��ꂽ���I';
		}
		else
		{
		$DT->{money}+=$pr;
		$DT->{saletoday}+=$pr;
		$disp.=$AucImg.'���ꂪ�����'.GetMoneyString($pr).'���B<br>';
		$disp.=$DT[$id2idx{$mode}]->{shopname}.'���񂪕����Ă��ꂽ���I';
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

