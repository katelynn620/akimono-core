# �Z��f�[�^�ҏW 2003/10/08 �R��

if ($Q{mode} eq 'new')
{
ProposeEdit();
DataWrite();
}
else
{
$i=SearchBride($Q{idx});
OutError('�w�肳�ꂽ���͑��݂��܂���') if ($i==-1);
($ida,$idb)=($BRIDE[$i]->{ida},$BRIDE[$i]->{idb});
}

$Q{mode}='mplus' if ($Q{mode} eq 'plus')&&($Q{it} == -1);	#�}�l�[���[�h�ɐؑ�
$Q{mode}='mminus' if ($Q{mode} eq 'minus')&&($Q{it} == -1);	#�}�l�[���[�h�ɐؑ�

if ($Q{mode} eq 'agree') {
	OutError($image[3].'�����ɕK�v�Ȏ���������܂���B') if ($DT->{money} < 5000000) ;
	$DT->{money}-=5000000;
	($BRIDE[$i]->{tm},$BRIDE[$i]->{mode},$BRIDE[$i]->{money})=($NOW_TIME,1,10000000);
	PushLog(3,0,$DT->{name}.' ('.$DT->{shopname}.')�� '.$DT[$id2idx{$ida}]->{name}.' ('.$DT[$id2idx{$ida}]->{shopname}.')�̌����̐\�����݂��󂯂܂����B');
	PushLog(1,0,$DT[$id2idx{$ida}]->{name}.' ('.$DT[$id2idx{$ida}]->{shopname}.')�� '.$DT->{name}.' ('.$DT->{shopname}.') ���������܂����B');
	DataWrite();
}
if ($Q{mode} eq 'end') {
	$DT->{money}+=5000000;	#������ԋp�B
	PushLog(3,0,$DT->{name}.' ('.$DT->{shopname}.')�� '.$DT[$id2idx{$idb}]->{name}.' ('.$DT[$id2idx{$idb}]->{shopname}.')�ւ̌����̐\�����݂��Ƃ��߂܂����B');
	$BRIDE[$i]->{mode}=-1;
	DataWrite();
}
if ($Q{mode} eq 'con') {
	OutError($image[3].'�Z��݂ɕK�v�Ȏ���������܂���B') if ($BRIDE[$i]->{money} < 15000000) ;
	my $check=0;
	foreach (0..$Scount) {
		$check=1 if ($BRIDE[$_]->{place}==$Q{place});
		}
	OutError($image[3].'���łɏZ����Ă��Ă���悤�ł��B') if ($check || $BRIDE[$i]->{place}) ;
	$BRIDE[$i]->{money}-=15000000;
	($BRIDE[$i]->{place},$BRIDE[$i]->{mode},$BRIDE[$i]->{reform})=($Q{place},3,'a');
	PushLog(2,0,$DT[$id2idx{$ida}]->{name}.'��'.$DT[$id2idx{$idb}]->{name}.'�v�Ȃ��Z������Ă܂����B');
}
if ($Q{mode} eq 'more') {
	OutError('���z�ł��܂���B') if ($BRIDE[$i]->{mode} < 2 || $BRIDE[$i]->{mode} > 7) ;
	OutError('�Z��z�ɕK�v�Ȏ���������܂���B') if ($BRIDE[$i]->{money} < $BRIDE[$i]->{mode} * 10000000);
	$BRIDE[$i]->{money}-=($BRIDE[$i]->{mode} * 10000000);
	$BRIDE[$i]->{mode}+=2;
	PushLog(2,0,$DT[$id2idx{$ida}]->{name}.'��'.$DT[$id2idx{$idb}]->{name}.'�v�Ȃ��Z��𑝒z���܂����B');
}
if ($Q{mode} eq 'plus') {
	$itemno=$Q{it};
	my $n=SearchBstock($Q{it});
	OutError('�ۊǃX�y�[�X������܂���B') if ($n == -1) ;
	my $space=$ITEM[$itemno]->{limit}*$HouseMax - $BRIDE[$i]->{cnt}[$n];
	OutError('�ۊǃX�y�[�X������܂���B') if ($space < 1) ;
	$Q{num}=$DT->{item}[$itemno-1] if ($Q{num} > $DT->{item}[$itemno-1]);
	$num=CheckCount($DT->{item}[$itemno-1],int($Q{num}),0,$space);
	OutError('�����Ȑ��l�w��ł��B') if !$num;
	$DT->{item}[$itemno-1]-=$num;
	$BRIDE[$i]->{stock}[$n]=$itemno;
	$BRIDE[$i]->{cnt}[$n]+=$num;
	DataWrite();
}
if ($Q{mode} eq 'minus') {
	my $n=$Q{it};
	my $itemno=$BRIDE[$i]->{stock}[$n];
	my $space=$ITEM[$itemno]->{limit} - $DT->{item}[$itemno-1];
	OutError('�q�ɂ���t�Ŏ��o���܂���B') if ($space < 1) ;
	$Q{num}=$BRIDE[$i]->{cnt}[$n] if ($Q{num} > $BRIDE[$i]->{cnt}[$n]);
	$num=CheckCount($BRIDE[$i]->{cnt}[$n],int($Q{num}),0,$space);
	OutError('�����Ȑ��l�w��ł��B') if !$num;
	$DT->{item}[$itemno-1]+=$num;
	$BRIDE[$i]->{cnt}[$n]-=$num;
	$BRIDE[$i]->{stock}[$n]=0 if !($BRIDE[$i]->{cnt}[$n]);
	DataWrite();
}
if ($Q{mode} eq 'mplus') {
	my $space=$BRIDE[$i]->{mode}*20000000 - $BRIDE[$i]->{money};
	OutError('�ۊǃX�y�[�X������܂���B') if ($space < 1) ;
	$Q{num}=$DT->{money} if ($Q{num} > $DT->{money});
	$num=CheckCount($DT->{money},int($Q{num}),0,$space);
	OutError('�����Ȑ��l�w��ł��B') if !$num;
	$DT->{money}-=$num;
	$BRIDE[$i]->{money}+=$num;
	DataWrite();
}
if ($Q{mode} eq 'mminus') {
	my $space=$MAX_MONEY - $DT->{money};
	OutError('�q�ɂ���t�Ŏ��o���܂���B') if ($space < 1) ;
	$Q{num}=$BRIDE[$i]->{money} if ($Q{num} > $BRIDE[$i]->{money});
	$num=CheckCount($BRIDE[$i]->{money},int($Q{num}),0,$space);
	OutError('�����Ȑ��l�w��ł��B') if !$num;
	$DT->{money}+=$num;
	$BRIDE[$i]->{money}-=$num;
	DataWrite();
}
if ($Q{mode} eq 'divorce') {
	$BRIDE[$i]->{mode}=-1;
	PushLog(1,0,$DT[$id2idx{$ida}]->{name}.' ('.$DT[$id2idx{$ida}]->{shopname}.')�� '.$DT[$id2idx{$idb}]->{name}.' ('.$DT[$id2idx{$idb}]->{shopname}.') ���������܂����B');
}
if ($Q{mode} eq 'dis') {
	$BRIDE[$i]->{mode}=-1;
	PushLog(3,0,$DT->{name}.' ('.$DT->{shopname}.')�� '.$DT[$id2idx{$ida}]->{name}.' ('.$DT[$id2idx{$ida}]->{shopname}.')�̌����̐\�����݂�f��܂����B');
}
WriteBride();
RenewLog();
DataCommitOrAbort();
UnLock();
1;


sub ProposeEdit
{
	my $check=0;
	OutError($image[3].'���C�͋֕��ł���B') if ($married) ;
	OutError($image[3].'�����ɕK�v�Ȏ���������܂���B') if ($DT->{money} < 5000000) ;
	my $tg=$Q{tg};
	OutError($image[3].'�����ƌ������邱�Ƃ͂ł��܂���B') if ($DT->{id} == $tg) ;
	foreach (0..$Scount) {
		$check=1 if ($tg==$BRIDE[$_]->{ida}) || ($tg==$BRIDE[$_]->{idb});
		}
	OutError($image[3].'���̐l��I�Ԃ��Ƃ͂����ł��܂����B') if ($check) ;
	$DT->{money}-=5000000;
	PushLog(3,0,$DT->{name}.' ('.$DT->{shopname}.')�� '.$DT[$id2idx{$tg}]->{name}.' ('.$DT[$id2idx{$tg}]->{shopname}.')�Ɍ�����\�����݂܂����B');
	@BRIDE=reverse(@BRIDE);
	$Scount++;
	my $i=$Scount;
	$BRIDE[$i]->{point}=0;
	$BRIDE[$i]->{no}=($i > 0) ? ($BRIDE[$i-1]->{no} + 1) : 1;
	($BRIDE[$i]->{tm},$BRIDE[$i]->{mode},$BRIDE[$i]->{ida},$BRIDE[$i]->{idb},$BRIDE[$i]->{money},$BRIDE[$i]->{place},$BRIDE[$i]->{reform})=($NOW_TIME,0,$DT->{id},$tg,0,0,0);
	$BRIDE[$i]->{stock}=(); $BRIDE[$i]->{stock}[0]=0;
	$BRIDE[$i]->{cnt}=(); $BRIDE[$i]->{cnt}[0]=0;
	@BRIDE=reverse(@BRIDE);
}

sub SearchBstock
{
	my($no)=@_;
	foreach(0..$BRIDE[$i]->{mode}-1)
	{
		return $_ if($no == $BRIDE[$i]->{stock}[$_]);	# �܂����łɕۊǂ���Ă��镨�Ɠ��������ׂ�
	}
	foreach(0..$BRIDE[$i]->{mode}-1)
	{
		return $_ if !($BRIDE[$i]->{stock}[$_]);	# ���ɋ󂫂����邩���ׂ�
	}
	return -1;
}

sub WriteBride
{
	my @buf;
	foreach my $i(0..$Scount)
		{
		next if ($BRIDE[$i]->{mode}==-1) || !defined($BRIDE[$i]->{no});
		$BRIDE[$i]->{stbase}=join(":",@{$BRIDE[$i]->{stock}});
		$BRIDE[$i]->{ctbase}=join(":",@{$BRIDE[$i]->{cnt}});
		$buf[$i]=join(",",map{$BRIDE[$i]->{$_}}@BRIDEnamelist)."\n";
		}
	OpenAndCheck(GetPath($TEMP_DIR,"bride"));
	print OUT @buf;
	close(OUT);
}
