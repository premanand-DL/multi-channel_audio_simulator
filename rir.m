function [ ] = rir(num_spk,num_chn,fs,r,s,L,t60,rooms,arr_type)
%str2num(num_spk)
%str2num(num_chn)
%str2num(fs)
%str2num(r)
%str2num(s)
%str2num(L)
%str2num(t60)
%num_chn = 3;
c = 340;                    % Sound velocity (m/s)
%fs = 16000;                 % Sample frequency (samples/s)
%r = [2.45 2.5 2 ; 2.5 2.5 2;2.55 2.5 2];    % Receiver positions [x_1 y_1 z_1 ; x_2 y_2 z_2] (m)
%s = [2 3.5 2;2,1.5,2];              % Source position [x y z] (m)
%L = [5 4 6];                % Room dimensions [x y z] (m)
beta = t60 ;               % Reverberation time (s)
n = 4096;                   % Number of samples
mtype = 'omnidirectional';  % Type of microphone
orders = -1;                 % -1 equals maximum reflection order!
dim = 3;                    % Room dimension
orientation = 0;            % Microphone orientation (rad)
hp_filter = 1;              % Enable high-pass filter
output_dir = [pwd '/'];


%Code
rir= zeros(num_chn,n,num_spk);
disp(['Generating RIR for: No. Channels :' num2str(num_chn)])
disp(['                                No. Speakers :' num2str(num_spk)])
disp(['                                T60 :' num2str(t60)])
for i=1:num_spk
  rir(:,:,i) = rir_generator(c, fs, r, s(i,:), L, beta, n, mtype, orders, dim, orientation, hp_filter);
  %disp(size(out)) 
end

center = r(1,:);
save('-mat',['rir_' num2str(num_spk) '_' num2str(num_chn) '_' num2str(t60) '.mat'],'rir','num_spk','num_chn','L','t60','fs','rooms','arr_type','s','orders','center')
%%
%fileid = fopen('spkid');
%fileids = textscan(fileid,'%d16');
%ids = fileids{1,1};
%sil = zeros(1,fs*1);


    %id = ids(round(rand(1)*length(ids)));
    %path = ['/media/Sharedata/DATASETS/LibriSpeech/train-clean-100/' num2str(id) ] ;
    %listdir = dir([path '/**/*.flac']);
    %file_pick = round(rand(1)*length(listdir));
    %path = [listdir(file_pick).folder '/' listdir(file_pick).name ];
    %[y,~] = audioread(path);
    
    %multi_spk = [] ;
    %for i=1:num_chn
      %output = [sil conv(y,h(i,:))'];
      %multi_spk = [multi_spk;output];
    %end
   %multi_audio = [multi_audio multi_spk];  

%audiowrite([output_dir 'multi_audio.wav'],multi_audio',fs);

endfunction

