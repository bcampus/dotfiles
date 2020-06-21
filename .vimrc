syntax on

" basic config variables
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set number relativenumber
set wildmode=longest,list,full
set scrolloff=15

" disable autocomment
autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

let mapleader=" "


" plugins
call plug#begin('~/.vim/plugged')
    Plug 'junegunn/goyo.vim'
    Plug 'jreybert/vimagit'
    Plug 'jremmen/vim-ripgrep'
    Plug 'tpope/vim-fugitive'
    Plug 'Valloric/YouCompleteMe'
    Plug 'mbbill/undotree'
call plug#end()

if executable('rg')
    let g:rg_derive_root='true'
endif

" goyo plugin binding
map <leader>f :Goyo \| set linebreak<CR>

" spellcheck binding
map <leader>o :setlocal spell! spelllang=en_gb<CR>

nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>
nnoremap <leader>u :UndotreeShow<CR>
nnoremap <leader>pv :wincmd v<bar> :Ex <bar> :vertical resize 30<CR>
nnoremap <Leader>ps :Rg<SPACE>


