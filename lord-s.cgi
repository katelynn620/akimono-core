# �̎�@ 2004/01/20 �R��

$image[0]=GetTagImgKao("��b","minister");
Lock();
DataRead();
CheckUserPass();

my $functionname=$Q{mode};
OutError("bad request") if !defined(&$functionname);
&$functionname;
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

OutSkin();
1;

sub inside
{
if ($Q{taxrate} =~ /([^0-9])/
	|| $Q{devem} =~ /([^0-9])/
	|| $Q{safem} =~ /([^0-9])/
	) { OutError('�g�p�ł��镶���͔��p���������ł�'); }
OutError($image[0].'�����牽�ł�����͍������Ƃ������̂ł����B') if ($Q{taxrate} > 40) ;
OutError($image[0].'��x�ɂ��ꂾ���΍����������ł����Ӗ��ł����B') if ($Q{devem} > 10000000 || $Q{safem} > 10000000) ;

$Q{taxrate}=0 if $Q{taxrate}<0;
$Q{devem}=0 if $Q{devem}<0;
$Q{safem}=0 if $Q{safem}<0;
my $taxrate=int($Q{taxrate});
$disp.="�X�̓������j��ύX���܂����B";

if ($DTTaxrate != $taxrate )
	{
	my $i="�����グ�܂���";
	$i="���������܂���" if $DTTaxrate > $taxrate;
	$DTTaxrate=int($Q{taxrate});
	PushLog(2,0,"�̎�".$DT->{name}."�͊X�̐ŗ���$taxrate%��$i�B");
	$disp.="<br>�X�̐ŗ���$taxrate%��$i�B";
	}
$STATE->{devem}=int($Q{devem});
$STATE->{safem}=int($Q{safem});
}

sub outside
{
OutError('�������̂��ߌٗp�ł��܂���B') if $DTevent{rebel};
my $stock=int($STATE->{money} / 1200);
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$stock);
OutError('�ٗp�l�����w�肵�Ă�������') if !$count;
$STATE->{money}-=$count * 1200;
$STATE->{army}+=$count;
$disp.="��q�R��$count�l�ق��܂����B";
}

sub outdel
{
OutError('�������̂��߉��قł��܂���B') if $DTevent{rebel};
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$STATE->{army});
OutError('���ِl�����w�肵�Ă�������') if !$count;
$STATE->{army}-=$count;
$disp.="��q�R��$count�l���ق��܂����B";
}

sub taxside
{
OutError('�ΏۓX��I�����Ă��������B') if !defined($id2idx{$Q{tg}});
my $i=$id2idx{$Q{tg}};
if ($Q{md} eq "free")
	{
	PushLog(2,0,"�̎�".$DT->{name}."��".$DT[$i]->{shopname}."�̐ł�Ə����܂����B") if ($DT[$i]->{taxmode}!=1);
	$DT[$i]->{taxmode}=1;
	$disp.=$DT[$i]->{shopname}."�̐ł�Ə����܂����B";
	}
elsif ($Q{md} eq "double")
	{
	PushLog(2,0,"�̎�".$DT->{name}."��".$DT[$i]->{shopname}."�̐ŗ���{�ɂ��܂����B") if ($DT[$i]->{taxmode}!=2);
	$DT[$i]->{taxmode}=2;
	$disp.=$DT[$i]->{shopname}."�̐ŗ���{�ɂ��܂����B";
	}
	else
	{
	PushLog(2,0,"�̎�".$DT->{name}."��".$DT[$i]->{shopname}."�̖Ɛł�����߂܂����B") if ($DT[$i]->{taxmode}==1);
	PushLog(2,0,"�̎�".$DT->{name}."��".$DT[$i]->{shopname}."�̔{�ł�����߂܂����B") if ($DT[$i]->{taxmode}==2);
	delete $DT[$i]->{taxmode};
	$disp.=$DT[$i]->{shopname}."�̐ł�ʏ�ɖ߂��܂����B";
	}
}

sub treset
{
foreach (@DT) {
	delete $_->{taxmode};
}
PushLog(2,0,"�̎�".$DT->{name}."�͔{�ł�Ɛł����ׂĎ���߂܂����B");
$disp.="�S�Ă̓X�̐ŗ���ʏ�ɖ߂��܂����B";
}

sub expose
{
OutError('�������̂��ߎ��s�ł��܂���B') if $DTevent{rebel};
OutError('�ΏۓX��I�����Ă��������B') if !defined($id2idx{$Q{tg}});
OutError('��p������܂���B') if ($STATE->{money} < 1000000);
my $i=$id2idx{$Q{tg}};
OutError($image[0].'���̓X�܂ɑ΂�������܂�͂��܂�Ӗ����Ȃ��悤�ł����B') if ($DT[$i]->{rank} < 2000) ;
$STATE->{money}-=1000000;
$DT[$i]->{rank}=int($DT[$i]->{rank} / 10);
$STATE->{safety}+=500;
$STATE->{safety}=10000 if $STATE->{safety} > 10000;
PushLog(2,0,"�̎�".$DT->{name}."��".$DT[$i]->{shopname}."�ɑ΂��Ď����܂���s���܂����B");
$disp.=$DT[$i]->{shopname}."�ɑ΂��Ď����܂���s���܂����B";
}

