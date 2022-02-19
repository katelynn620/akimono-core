# �Ǘ��@�\������ 2003/09/25 �R��

my $functionname=$Q{mode};
OutError("�s���ȃ��N�G�X�g�ł�") if !defined(&$functionname);
&$functionname;

sub menteon
{
	if(-d "$DATA_DIR/lock")
		{push(@log,'���݃����e���[�h�ł�');}
	elsif(mkdir("$DATA_DIR/lock",$DIR_PERMISSION))
		{push(@log,'�����e���[�h�ɓ���܂���');}
	else
		{push(@log,'�����e���[�h�Ɉڍs�ł��܂���ł���',$checkdatadir);}
}

sub menteoff
{
	if(!-d "$DATA_DIR/lock")
		{push(@log,'���݃����e���[�h�ł͂���܂���');}
	elsif(rmdir("$DATA_DIR/lock"))
		{push(@log,'�����e���[�h���������܂���');}
	else
		{push(@log,'�����e���[�h�̉����Ɏ��s���܂���',$checkdatadir);}
}

sub errdel
{
	unlink("$DATA_DIR/error.log");
	push(@log,'�G���[�����폜���܂����B');
}

sub init
{
	CheckLock();
	#�e��f�B���N�g�����_�~�[index.html �쐬
	foreach my $dir ($COMMON_DIR,$DATA_DIR,$SESSION_DIR,$COTEMP_DIR,$TEMP_DIR,$LOG_DIR,$SUBDATA_DIR,$BACKUP_DIR)
	{
		if(!-d $dir)
		{
			if(mkdir($dir,$DIR_PERMISSION))
				{push(@log,'�f�B���N�g�� '.$dir.' ���쐬���܂���');}
			else
			{
				push(@log,'�f�B���N�g�� '.$dir.' �͍쐬�o���܂���ł���');
				push(@log,' �ݒ�����������A�蓮�ō쐬���Ă�������');
			}
		}
		if(!-e "$dir/index.html")
		{
			if(open(OUT,">$dir/index.html"))
			{
				print OUT "<html></html>";
				close(OUT);
				push(@log,'�f�B���N�g�� '.$dir.' �փ_�~�[��index.html���쐬���܂���');
			}
			else
			{
				push(@log,'�f�B���N�g�� '.$dir.' �ւ̃_�~�[index.html�쐬�Ɏ��s���܂���');
				push(@log,' �f�B���N�g�� '.$dir.' �̃p�[�~�b�V�������������Ă�������');
			}
		}
	}
	
	#���b�N�t�@�C���쐬
	if(!GetFileList($DATA_DIR,"^$LOCK_FILE"))
	{
		if(open(DATA,">$DATA_DIR/$LOCK_FILE"))
		{
			print DATA '���b�N�t�@�C���ł��B�폜���Ă͂����܂���B';
			close(DATA);
			push(@log,'���b�N�t�@�C�����쐬���܂���');
		}
		else
		{
			push(@log,'���b�N�t�@�C���̍쐬�Ɏ��s���܂���');
		}
	}
	if(!GetFileList($COMMON_DIR,"^$LOCK_FILE"))
	{
		if(open(DATA,">$COMMON_DIR/$LOCK_FILE"))
		{
			print DATA '���b�N�t�@�C���ł��B�폜���Ă͂����܂���B';
			close(DATA);
			push(@log,'���L���b�N�t�@�C�����쐬���܂���');
		}
		else
		{
			push(@log,'���L���b�N�t�@�C���̍쐬�Ɏ��s���܂���');
		}
	}
	
	#�^�E���f�[�^�쐬
	MakeTownFile();
	
	#�V�K�Q�[���f�[�^�쐬
	if(!-e "$DATA_DIR/$DATA_FILE$FILE_EXT")
	{
		if(open(DATA,">$DATA_DIR/$DATA_FILE$FILE_EXT"))
		{
			print DATA time()."\n500000,100,,0,0:0:0:0:5001:0:5001:0:0:2000:0\n\n\n//\n"; #�������
			close(DATA);
			unlink(map{"$DATA_DIR/$_$FILE_EXT"}grep($_ ne $DATA_FILE,@BACKUP_FILES)); #�֘A�t�@�C��������������
			push(@log,'�Q�[���f�[�^��V�K�쐬���܂���');
		}
		else
			{push(@log,'�Q�[���f�[�^�̐V�K�쐬�Ɏ��s���܂���',$checkdatadir);}
	}
	
	#�ŏI�X�V���������p�t�@�C���쐬
	MakeFile("$DATA_DIR/$LASTTIME_FILE$FILE_EXT",'�ŏI�X�V���������p�t�@�C��','');
	#�M���h��`�t�@�C���x�[�X�쐬
	MakeFile("$DATA_DIR/$GUILD_FILE$FILE_EXT",'�M���h��`�t�@�C��','1;');
	
	sub MakeFile
	{
		if(!-e $_[0])
		{
			if(open(DATA,">$_[0]"))
			{
				print DATA $_[2];
				close(DATA);
				utime(1,1,$_[0]);
				push(@log,$_[1].'���쐬���܂���');
			}
			else
				{push(@log,$_[1].'�쐬�Ɏ��s���܂���',$checkdatadir);}
		}
	}
	push(@log,'������/�C���̕K�v�͂���܂���ł����B') if !scalar(@log);
}

sub delunit
{
	CheckLock();
	delete_dir($DATA_DIR);
	push(@log,'�폜���ׂ��f�[�^������܂���ł����B') if !scalar(@log);
}

sub piece
{
	CheckLock();
	delete_evt();
	delete_dir($LOG_DIR,1);
	delete_dir($ITEM_DIR,1);
	delete_dir($SESSION_DIR,1);
	delete_dir($TEMP_DIR,1);
	delete_dir($SUBDATA_DIR,1);
	push(@log,'�폜���ׂ��f�[�^������܂���ł����B') if !scalar(@log);
}

sub mini
{
	CheckLock();
	delete_evt();
	delete_dir($ITEM_DIR,1);
	push(@log,'�폜���ׂ��f�[�^������܂���ł����B') if !scalar(@log);
}

sub timeedit
{
	CheckLock();
	$Q{tlyear}-=1900 if $Q{tlyear}>=2000;
	$time=0;
	$time=GetTimeLocal($Q{tlsec},$Q{tlmin},$Q{tlhour},$Q{tlday},$Q{tlmon}-1,$Q{tlyear});
	if(!$time) { push(@log,'���t�����ݒ肪�s���ł�');}
	elsif(open(IN,"$DATA_DIR/$DATA_FILE$FILE_EXT"))
	{
		my @data=<IN>;
		close(IN);
		$data[0]=$time."\n";
		open(OUT,">$DATA_DIR/$DATA_FILE$FILE_EXT");
		print OUT @data;
		close(OUT);
		my($s,$min,$h,$d,$m,$y)=gmtime($time+$TZ_JST);
		my $timestr=sprintf("%04d-%02d-%02d %02d:%02d:%02d",$y+1900,$m+1,$d,$h,$min,$s);
		push(@log,'�ŏI�X�V������['.$timestr.']�ɐݒ肵�܂���');
	}
	else
	{
		push(@log,'�f�[�^�t�@�C����ύX�o���܂���ł���');
	}
}

sub backup
{
	CheckLock();
	#�o�b�N�A�b�v�������ɕ���
	my @files=map{"$_$FILE_EXT"}@BACKUP_FILES;
	my @errorfiles=grep(!-e $_,map{"$Q{backup}/$_"}@files);
	
	if(scalar(@errorfiles))
	{
		push(@log,map{$_.' �����݂��܂���ł���'}@errorfiles);
		push(@log,'�o�b�N�A�b�v�f�[�^���s���S�Ȃ̂ŏ����𒆎~���܂���');
	}
	else
	{
		my $time=(stat("$Q{backup}/$DATA_FILE$FILE_EXT"))[9];
		my($s,$min,$h,$d,$m,$y)=gmtime($time+$TZ_JST);
		my $timestr=sprintf("%04d-%02d-%02d %02d:%02d",$y+1900,$m+1,$d,$h,$min);
		
		foreach my $file (@files)
		{
			my $inok=open(IN,"$Q{backup}/$file");
			my $outok=open(OUT,">$DATA_DIR/$file");
			if($inok && $outok)
			{
				my @data=<IN>;
				close(IN);
				if($file eq $DATA_FILE.$FILE_EXT)
				{
					#play.cgi�̏ꍇ�͍X�V���������݂�
					$data[0]=time()."\n";
					push(@log,'�ŏI�X�V���������݂ɐݒ肵�܂���');
				}
				if($file eq $LOG_FILE."-s0".$FILE_EXT || $file eq $PERIOD_FILE.$FILE_EXT)
				{
					#period.cgi��log-s0.cgi�̏ꍇ�̓o�b�N�A�b�v�����A�i�E���X��t��
					unshift(@data,time().",1,0,0,�o�b�N�A�b�v�f�[�^�����̂���[$timestr]���_�ɖ߂�܂���\n");
				}
				print OUT @data;
				close(OUT);
				push(@log,$file.' �̕����ɐ������܂���');
			}
			else
			{
				close(IN) if $inok;
				push(@log,$file.' �̕����Ɏ��s���܂���',' �ēx�������s���Ă�������');
			}
		}
	}
}

sub CheckLock
{
	return if -e "./lock" or -e "$DATA_DIR/lock";
	if(mkdir("$DATA_DIR/lock",$DIR_PERMISSION))
		{
		return;
		}
		else
		{
		OutError('���̑���̓����e���[�h�ł����s���܂���','noerror');
		}
}

sub GetTimeLocal {
    my($Sec, $Min, $Hour, $Date, $Mon, $Year) = @_;
    my($sec, $min, $hour, $date, $mon, $year, $day, $yday, $isdst);

    my($cnt) = 0;
    my($Now) = time;
    while($cnt < 20) {
        ($sec, $min, $hour, $date, $mon, $year, $day, $yday, $isdst) = gmtime($Now+$TZ_JST);
        if ($year != $Year) {
            $Now -= ($year - $Year) * 31536000;
        } elsif ($mon != $Mon) {
            $Now -= ($mon - $Mon) * 2592000;
        } elsif ($date != $Date) {
            $Now -= ($date - $Date) * 86400;
        } elsif ($hour != $Hour) {
            $Now -= ($hour - $Hour) * 3600;
        } elsif ($min != $Min) {
            $Now -= ($min - $Min) * 60;
        } elsif ($sec != $Sec) {
            $Now -= ($sec - $Sec);
        } else {
            last;
        }
        $cnt++;
    }
    $Now = 0 if $cnt == 20;

    return $Now;
}

sub delete_evt
{
	if(open(IN,"$DATA_DIR/$DATA_FILE$FILE_EXT"))
	{
	my @data=<IN>;
	close(IN);
	$data[3]="\n";
	open(OUT,">$DATA_DIR/$DATA_FILE$FILE_EXT");
	print OUT @data;
	close(OUT);
	push(@log,$DATA_FILE.$FILE_EXT.'���̃C�x���g�f�[�^���폜���܂���');
	}
	else
	{
	push(@log,' '.$DATA_FILE.$FILE_EXT.'���C�x���g�f�[�^�폜�Ɏ��s���܂���');
	}
}

sub delete_dir
{
	my($dir,$owndelete)=@_;
	
	return if !-d $dir;
	
	opendir(DIR,$dir);
	my @filelist=grep(!/^\.\.?$/,readdir(DIR));
	closedir(DIR);
	foreach my $file (@filelist)
	{
		$file="$dir/$file";
		if(-f $file)
		{
			if(unlink($file))
				{push(@log,$file.' ���폜���܂���');}
			else
				{push(@log,' '.$file.' �̍폜�Ɏ��s���܂���');}
		}
		delete_dir($file,1) if -d $file;
	}
	if($owndelete)
	{
		if(rmdir($dir))
			{push(@log,'�f�B���N�g�� '.$dir.' ���폜���܂���');}
		else
			{push(@log,' �f�B���N�g��'.$dir.' �̍폜�Ɏ��s���܂���');}
	}
}

sub MakeTownFile
{
my $townfile="$COMMON_DIR/towndata$FILE_EXT";
require $townfile if -e $townfile;

return if ($Tname{$MYDIR} eq $TOWN_TITLE);

	if(open(OUT,">".$townfile))
		{
		$Tname{$MYDIR}=$TOWN_TITLE;
		undef @OtherDir;
		@OtherDir=keys(%Tname);
		print OUT '@OtherDir=("',join('","',@OtherDir),'");',"\n";
		foreach(keys(%Tname))
			{
			print OUT '$Tname{',$_,'}="',$Tname{$_},'";',"\n";
			}
			close(OUT);
			push(@log,'�X���X�g���쐬���܂���');
		}
		else
		{
			push(@log,'�X���X�g�̍쐬�Ɏ��s���܂���'.$townfile);
		}
}
1;
