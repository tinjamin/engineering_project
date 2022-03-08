set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent 
set nu
set relativenumber
set nohlsearch
set incsearch 
set scrolloff=8
set linebreak 
set foldenable
set cmdheight=2
set updatetime=300
set signcolumn=yes
filetype plugin on 
syntax on 
set nocompatible 

" Changing gj and gk 
nnoremap <expr> j v:count ? (v:count > 5 ? "m'" . v:count : '') . 'j' : 'gj'
nnoremap <expr> k v:count ? (v:count > 5 ? "m'" . v:count : '') . 'k' : 'gk'

"..................................................................
" Custom mapping
"..................................................................

let mapleader = ' '

" Windows navigation 
:nnoremap <leader>h <C-w>h
:nnoremap <leader>j <C-w>j
:nnoremap <leader>k <C-w>k
:nnoremap <leader>l <C-w>l

" Delete entire word
inoremap ∑ <C-w>

" Remap Esc Key 
inoremap jk <Esc>

" Scrolling through recommendations
inoremap ≥ <C-n>
inoremap ≤ <C-p>

"..................................................................
" Plug-in Manager 
"..................................................................

call plug#begin('~/.config/nvim/plugged')
Plug 'SirVer/ultisnips'
Plug 'morhetz/gruvbox'
Plug 'jiangmiao/auto-pairs'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'scrooloose/nerdtree'
call plug#end()

let g:UltiSnipsExpandTrigger="ß"
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"

"COC.nvim config 
let g:coc_global_extensions = ['coc-css', 'coc-html', 'coc-prettier']

" Use tab for trigger completion with characters ahead and navigate.
" Use command ':verbose imap <tab>' to make sure tab is not mapped by other plugin.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
inoremap <silent><expr> <C-space> coc#refresh()

" Use K to show documentation in preview window
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

" Make <CR> auto-select the first completion item and notify coc.nvim to
" format on enter, <cr> could be remapped by other vim plugin
inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

"NERDTree config
let g:NERDTreeShowHidden = 1
let g:NERDTreeMinimalUI = 1
let g:NERDTreeIgnore = []
let g:NERDTreeStatusline = ''
nnoremap <silent> <leader>e :NERDTreeToggle<CR> 

" Gruvbox colorscheme 
colorscheme gruvbox
" Remove highlight for _ in Markdown
highlight link markdownError htmlLink 

" https://betterprogramming.pub/setting-up-neovim-for-web-development-in-2020-d800de3efacd
" open new split panes to right and below
set splitright
set splitbelow
" turn terminal to normal mode with escape
tnoremap <Esc> <C-\><C-n>
" start terminal in insert mode
au BufEnter * if &buftype == 'terminal' | :startinsert | endif
" open terminal on ctrl+n
function! OpenTerminal()
  split term://zsh
  resize 10
endfunction
nnoremap <leader>t :call OpenTerminal()<CR>
