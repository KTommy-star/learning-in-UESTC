// 音频播放器功能
class MusicPlayer {
    constructor() {
        this.audioPlayer = document.getElementById('audioPlayer');
        this.playBtn = document.getElementById('playBtn');
        this.uploadBtn = document.getElementById('uploadBtn');
        this.volumeBtn = document.getElementById('volumeBtn');
        this.volumeSlider = document.getElementById('volumeSlider');
        this.musicFile = document.getElementById('musicFile');
        this.musicInfo = document.getElementById('musicInfo');
        this.isPlaying = false;
        this.isMuted = false;
        this.init();
    }

    init() {
        this.bindEvents();
        this.audioPlayer.volume = 0.5;
    }

    bindEvents() {
        // 上传按钮点击
        this.uploadBtn.addEventListener('click', () => {
            this.musicFile.click();
        });

        // 文件选择
        this.musicFile.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) {
                this.loadMusic(file);
            }
        });

        // 播放/暂停按钮
        this.playBtn.addEventListener('click', () => {
            this.togglePlay();
        });

        // 音量按钮
        this.volumeBtn.addEventListener('click', () => {
            this.toggleMute();
        });

        // 音量滑块
        this.volumeSlider.addEventListener('input', (e) => {
            this.setVolume(e.target.value / 100);
        });

        // 音频事件
        this.audioPlayer.addEventListener('loadeddata', () => {
            this.playBtn.disabled = false;
        });

        this.audioPlayer.addEventListener('ended', () => {
            this.isPlaying = false;
            this.playBtn.textContent = '▶️';
        });

        this.audioPlayer.addEventListener('error', () => {
            this.musicInfo.textContent = '音频加载失败';
            this.playBtn.disabled = true;
        });
    }

    loadMusic(file) {
        const url = URL.createObjectURL(file);
        this.audioPlayer.src = url;
        this.musicInfo.textContent = file.name.replace(/\.[^/.]+$/, '');
        this.playBtn.disabled = false;
    }

    togglePlay() {
        if (this.isPlaying) {
            this.audioPlayer.pause();
            this.playBtn.textContent = '▶️';
        } else {
            this.audioPlayer.play();
            this.playBtn.textContent = '⏸️';
        }
        this.isPlaying = !this.isPlaying;
    }

    toggleMute() {
        if (this.isMuted) {
            this.audioPlayer.muted = false;
            this.volumeBtn.textContent = '🔊';
            this.volumeSlider.style.opacity = '1';
        } else {
            this.audioPlayer.muted = true;
            this.volumeBtn.textContent = '🔇';
            this.volumeSlider.style.opacity = '0.5';
        }
        this.isMuted = !this.isMuted;
    }

    setVolume(volume) {
        this.audioPlayer.volume = volume;
        if (volume === 0) {
            this.volumeBtn.textContent = '🔇';
        } else if (volume < 0.5) {
            this.volumeBtn.textContent = '🔉';
        } else {
            this.volumeBtn.textContent = '🔊';
        }
    }
}

// 时空隧道照片相册
class TunnelPhotoAlbum {
    constructor() {
        this.currentIndex = 0;
        // 使用HTML中定义的照片数据，如果不存在则使用默认数据
        this.photos = window.photoData || [
            {
                id: 1,
                title: '生日快乐',
                description: '愿你的每一天都充满阳光与快乐',
                emoji: '🎂',
                color: '#ff6b6b',
                image: '' // 预留图片字段
            }
        ];
        
        // 祝福语数据组合
        this.blessingsData = [
            {
                left: '我猜我应该是喜欢你了',
                right: '没有任何原因，也没办法说明'
            },
            {
                left: '我猜应该是上天的指引',
                right: '让我遇见了你，最好时候的你'
            },
            {
                left: '山河万里不及你',
                right: '愿你被这世界温柔以待'
            },
            {
                left: '春风十里不如你',
                right: '冬雪纷飞等待你'
            },
            {
                left: '愿你眼中有星辰',
                right: '不负韶华不负卿'
            },
            {
                left: '你是人间的四月天',
                right: '你是一树一树的花开'
            }
        ];
        
        this.isStarted = false;
        this.init();
    }
    
    init() {
        this.createStartupScreen();
        this.createTunnelContainer();
        this.bindEvents();
        this.createFloatingParticles();
    }

    createStartupScreen() {
        const startupScreen = document.querySelector('.startup-screen');
        if (startupScreen) {
            const startButton = startupScreen.querySelector('.start-button');
            if (startButton) {
                startButton.addEventListener('click', () => this.startAlbum());
            }
        }
    }

    createTunnelContainer() {
        const tunnelContainer = document.querySelector('.tunnel-container');
        if (!tunnelContainer) return;

        // 使用HTML中已存在的照片堆叠容器
        const photoStack = document.querySelector('.photo-stack');
        if (photoStack) {
            // 清空现有内容，然后创建照片卡片
            photoStack.innerHTML = '';
            
            // 创建所有照片卡片
            this.photos.forEach((photo, index) => {
                const photoCard = this.createPhotoCard(photo, index);
                photoStack.appendChild(photoCard);
            });
        }

        // 绑定HTML中已存在的控制按钮
        this.bindExistingControls();
    }

    // 绑定HTML中已存在的控制元素
    bindExistingControls() {
        // 绑定导航按钮
        const prevBtn = document.querySelector('.prev-btn');
        const nextBtn = document.querySelector('.next-btn');
        
        if (prevBtn) {
            prevBtn.addEventListener('click', () => this.previousPhoto());
        }
        
        if (nextBtn) {
            nextBtn.addEventListener('click', () => this.nextPhoto());
        }
        
        // 绑定返回按钮
        const backBtn = document.querySelector('.back-btn');
        if (backBtn) {
            backBtn.addEventListener('click', () => this.backToStart());
        }
        
        // 更新进度条
        this.updateProgress();
    }

    createPhotoCard(photo, index) {
        const card = document.createElement('div');
        card.className = 'photo-card';
        card.style.setProperty('--card-color', photo.color);
        
        // 可爱挂件数组
        const charms = ['🎀', '🌸', '🦋', '🌺', '🎈', '🌙', '⭐', '💖'];
        const ribbonColors = ['#ff6b9d', '#ffc3a0', '#a8e6cf', '#dcedc1'];
        
        // 根据是否有图片决定显示内容
        let mediaContent = '';
        if (photo.image && photo.image.trim() !== '') {
            mediaContent = `
                <div class="photo-image-container">
                    <img class="photo-image" src="${photo.image}" alt="${photo.title}" onerror="this.parentElement.innerHTML='<div class=\"photo-emoji\">${photo.emoji}</div>'">
                </div>
            `;
        } else {
            mediaContent = `<div class="photo-emoji">${photo.emoji}</div>`;
        }
        
        // 创建photo-content容器
        const photoContent = document.createElement('div');
        photoContent.className = 'photo-content';
        
        // 创建装饰容器
        const decorations = document.createElement('div');
        decorations.className = 'photo-decorations';
        decorations.innerHTML = `
            <!-- 角落装饰 -->
            <div class="decoration-corner top-left"></div>
            <div class="decoration-corner top-right"></div>
            <div class="decoration-corner bottom-left"></div>
            <div class="decoration-corner bottom-right"></div>
            
            <!-- 可爱挂件 -->
            <div class="decoration-charm top-left">${charms[index % charms.length]}</div>
            <div class="decoration-charm top-right">${charms[(index + 1) % charms.length]}</div>
            <div class="decoration-charm bottom-left">${charms[(index + 2) % charms.length]}</div>
            <div class="decoration-charm bottom-right">${charms[(index + 3) % charms.length]}</div>
            
            <!-- 彩带装饰 -->
            <div class="decoration-ribbon top"></div>
            <div class="decoration-ribbon bottom"></div>
            <div class="decoration-ribbon left"></div>
            <div class="decoration-ribbon right"></div>
            
            <!-- 闪烁星星 -->
            <div class="decoration-stars">⭐</div>
            <div class="decoration-stars">✨</div>
            <div class="decoration-stars">💫</div>
            <div class="decoration-stars">🌟</div>
            
            <!-- 原有装饰 -->
            <div class="decoration-sparkle">✨</div>
            <div class="decoration-sparkle">⭐</div>
            <div class="decoration-sparkle">💫</div>
            <div class="decoration-sparkle">🌟</div>
        `;
        
        // 创建媒体内容
        const mediaDiv = document.createElement('div');
        mediaDiv.innerHTML = mediaContent;
        
        // 创建标题
        const title = document.createElement('h2');
        title.className = 'photo-title';
        title.textContent = photo.title;
        console.log('创建标题:', photo.title);
        
        // 创建描述
        const description = document.createElement('p');
        description.className = 'photo-description';
        description.textContent = photo.description;
        console.log('创建描述:', photo.description);
        
        // 按新布局添加元素：标题(左) - 图片(中) - 描述(右)
        photoContent.appendChild(decorations);
        photoContent.appendChild(title);
        photoContent.appendChild(mediaDiv.firstElementChild || mediaDiv);
        photoContent.appendChild(description);
        
        card.appendChild(photoContent);
        
        // 确保标题和描述正确显示
        title.style.position = 'relative';
        description.style.position = 'relative';
        title.style.zIndex = '999';
        description.style.zIndex = '999';
        
        // 设置初始位置
        this.setCardPosition(card, index);
        
        return card;
    }

    setCardPosition(card, index) {
        const diff = index - this.currentIndex;
        
        card.classList.remove('current', 'next', 'prev', 'stack-back', 'hidden');
        
        if (diff === 0) {
            card.classList.add('current');
        } else if (diff === 1) {
            card.classList.add('next');
        } else if (diff === -1) {
            card.classList.add('prev');
        } else if (Math.abs(diff) === 2) {
            card.classList.add('stack-back');
        } else {
            card.classList.add('hidden');
        }
    }

    createControls(container) {
        const controls = document.createElement('div');
        controls.className = 'controls';
        
        const prevBtn = document.createElement('button');
        prevBtn.className = 'nav-btn';
        prevBtn.innerHTML = '‹';
        prevBtn.addEventListener('click', () => this.previousPhoto());
        
        const nextBtn = document.createElement('button');
        nextBtn.className = 'nav-btn';
        nextBtn.innerHTML = '›';
        nextBtn.addEventListener('click', () => this.nextPhoto());
        
        controls.appendChild(prevBtn);
        controls.appendChild(nextBtn);
        
        container.appendChild(controls);
    }

    createProgressBar(container) {
        const progressBar = document.createElement('div');
        progressBar.className = 'progress-bar';
        
        const progressFill = document.createElement('div');
        progressFill.className = 'progress-fill';
        
        progressBar.appendChild(progressFill);
        container.appendChild(progressBar);
        
        this.updateProgress();
    }

    createBackButton(container) {
        const backBtn = document.createElement('button');
        backBtn.className = 'back-btn';
        backBtn.textContent = '返回';
        backBtn.addEventListener('click', () => this.backToStart());
        
        container.appendChild(backBtn);
    }

    startAlbum() {
        if (this.isStarted) return;
        
        this.isStarted = true;
        
        // 添加远近拉伸镜头感切换动画到启动界面
        const startupScreen = document.querySelector('.startup-screen');
        if (startupScreen) {
            startupScreen.classList.add('zoom-out-transition');
            
            // 延迟隐藏启动界面
            setTimeout(() => {
                startupScreen.style.display = 'none';
                startupScreen.classList.remove('zoom-out-transition');
            }, 500);
        }
        
        // 显示隧道容器并添加远近拉伸镜头感切换动画
        const tunnelContainer = document.querySelector('.tunnel-container');
        if (tunnelContainer) {
            // 稍微延迟显示，避免黑屏
            setTimeout(() => {
                tunnelContainer.style.display = 'block';
                tunnelContainer.classList.add('zoom-in-transition');
                
                // 初始化照片堆叠
                this.initializeStack();
                
                // 延迟启动自动播放
                setTimeout(() => {
                    this.startAutoSlideshow();
                }, 200);
                
                // 动画完成后清理类名
                setTimeout(() => {
                    tunnelContainer.classList.remove('zoom-in-transition');
                }, 500);
            }, 100);
        }
        
        // 创建进入动画
        this.createEntranceEffect();
        
        // 初始化祝福语
        this.updateBlessings();
    }

    createEntranceEffect() {
        // 创建星光粒子效果
        for (let i = 0; i < 20; i++) {
            setTimeout(() => {
                this.createStarParticle();
            }, i * 100);
        }
    }

    createStarParticle() {
        const particle = document.createElement('div');
        particle.style.position = 'fixed';
        particle.style.pointerEvents = 'none';
        particle.style.zIndex = '999';
        particle.style.fontSize = '20px';
        particle.textContent = '✨';
        
        const x = Math.random() * window.innerWidth;
        const y = Math.random() * window.innerHeight;
        
        particle.style.left = x + 'px';
        particle.style.top = y + 'px';
        
        document.body.appendChild(particle);
        
        // 动画
        particle.animate([
            { 
                transform: 'scale(0) rotate(0deg)',
                opacity: 0
            },
            { 
                transform: 'scale(1.5) rotate(180deg)',
                opacity: 1,
                offset: 0.5
            },
            { 
                transform: 'scale(0) rotate(360deg)',
                opacity: 0
            }
        ], {
            duration: 2000,
            easing: 'ease-out'
        }).onfinish = () => {
            particle.remove();
        };
    }

    nextPhoto() {
        // 实现循环切换：到达最后一张时回到第一张
        this.currentIndex = (this.currentIndex + 1) % this.photos.length;
        this.updatePhotoStack();
        this.createTransitionEffect('next');
    }

    previousPhoto() {
        // 实现循环切换：在第一张时跳到最后一张
        this.currentIndex = (this.currentIndex - 1 + this.photos.length) % this.photos.length;
        this.updatePhotoStack();
        this.createTransitionEffect('prev');
    }

    updatePhotoStack() {
        const cards = document.querySelectorAll('.photo-card');
        cards.forEach((card, index) => {
            this.setCardPosition(card, index);
        });
        
        this.updateControls();
        this.updateProgress();
        
        // 更新悬浮祝福语
        this.updateBlessings();
    }

    updateControls() {
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        
        // 循环切换模式下，按钮始终可用
        if (prevBtn) prevBtn.disabled = false;
        if (nextBtn) nextBtn.disabled = false;
    }

    // 更新悬浮祝福语
    updateBlessings() {
        const leftBlessings = document.getElementById('leftBlessings');
        const rightBlessings = document.getElementById('rightBlessings');
        
        if (leftBlessings && rightBlessings) {
            // 先添加滑出动画
            leftBlessings.querySelectorAll('.ancient-blessing').forEach(text => {
                if (text.classList.contains('active')) {
                    text.classList.add('slide-out');
                    text.classList.remove('active');
                }
            });
            rightBlessings.querySelectorAll('.ancient-blessing').forEach(text => {
                if (text.classList.contains('active')) {
                    text.classList.add('slide-out');
                    text.classList.remove('active');
                }
            });
            
            // 更新祝福语位置 - 上中下循环
            const positions = ['position-top', 'position-middle', 'position-bottom'];
            const positionIndex = this.currentIndex % positions.length;
            const currentPosition = positions[positionIndex];
            
            // 移除所有位置类
            leftBlessings.classList.remove('position-top', 'position-middle', 'position-bottom');
            rightBlessings.classList.remove('position-top', 'position-middle', 'position-bottom');
            
            // 添加当前位置类
            leftBlessings.classList.add(currentPosition);
            rightBlessings.classList.add(currentPosition);
            
            // 延迟更新祝福语内容并显示滑入动画
            setTimeout(() => {
                // 根据当前照片索引选择祝福语组合
                const blessingIndex = this.currentIndex % this.blessingsData.length;
                const currentBlessings = this.blessingsData[blessingIndex];
                
                // 更新左侧祝福语内容（只显示第一条）
                const leftTexts = leftBlessings.querySelectorAll('.ancient-blessing');
                if (leftTexts[0]) {
                    leftTexts[0].classList.remove('slide-out');
                    leftTexts[0].textContent = currentBlessings.left;
                    leftTexts[0].classList.add('active');
                }
                
                // 更新右侧祝福语内容（只显示第一条）
                const rightTexts = rightBlessings.querySelectorAll('.ancient-blessing');
                if (rightTexts[0]) {
                    rightTexts[0].classList.remove('slide-out');
                    rightTexts[0].textContent = currentBlessings.right;
                    rightTexts[0].classList.add('active');
                }
            }, 600); // 等待滑出动画完成
        }
    }

    // 更新进度条
    updateProgress() {
        const progressFill = document.getElementById('progressFill');
        if (progressFill) {
            const progress = ((this.currentIndex + 1) / this.photos.length) * 100;
            progressFill.style.width = `${progress}%`;
        }
    }

    createTransitionEffect(direction) {
        // 创建过渡粒子效果
        for (let i = 0; i < 10; i++) {
            setTimeout(() => {
                this.createTransitionParticle(direction);
            }, i * 50);
        }
        
        // 添加震动效果
        const photoStack = document.querySelector('.photo-stack');
        if (photoStack) {
            photoStack.style.animation = 'none';
            photoStack.offsetHeight; // 触发重排
            photoStack.style.animation = 'stackShake 0.3s ease-out';
            
            setTimeout(() => {
                photoStack.style.animation = '';
            }, 300);
        }
    }

    createTransitionParticle(direction) {
        const particle = document.createElement('div');
        particle.style.position = 'fixed';
        particle.style.pointerEvents = 'none';
        particle.style.zIndex = '50';
        particle.style.fontSize = '16px';
        particle.textContent = direction === 'next' ? '→' : '←';
        particle.style.color = '#fff';
        
        const startX = direction === 'next' ? 0 : window.innerWidth;
        const endX = direction === 'next' ? window.innerWidth : 0;
        const y = window.innerHeight / 2 + (Math.random() - 0.5) * 200;
        
        particle.style.left = startX + 'px';
        particle.style.top = y + 'px';
        
        document.body.appendChild(particle);
        
        particle.animate([
            { 
                left: startX + 'px',
                opacity: 0,
                transform: 'scale(0)'
            },
            { 
                opacity: 1,
                transform: 'scale(1)',
                offset: 0.2
            },
            { 
                left: endX + 'px',
                opacity: 0,
                transform: 'scale(0)'
            }
        ], {
            duration: 1000,
            easing: 'ease-out'
        }).onfinish = () => {
            particle.remove();
        };
    }

    initializeStack() {
        // 初始化照片堆叠显示
        this.updatePhotoStack();
        this.updateControls();
        this.updateProgressBar();
    }

    startAutoSlideshow() {
        // 自动播放功能（可选）
        this.autoSlideInterval = setInterval(() => {
            if (this.currentIndex < this.photos.length - 1) {
                this.nextPhoto();
            } else {
                clearInterval(this.autoSlideInterval);
            }
        }, 4000);
    }

    stopAutoSlideshow() {
        if (this.autoSlideInterval) {
            clearInterval(this.autoSlideInterval);
            this.autoSlideInterval = null;
        }
    }

    backToStart() {
        this.stopAutoSlideshow();
        
        // 先显示启动界面，避免黑屏
        const startupScreen = document.querySelector('.startup-screen');
        if (startupScreen) {
            startupScreen.style.display = 'flex';
            startupScreen.style.opacity = '0';
            startupScreen.style.transform = 'scale(1.2)';
        }
        
        // 添加远近拉伸退出动画到隧道容器
        const tunnelContainer = document.querySelector('.tunnel-container');
        if (tunnelContainer) {
            tunnelContainer.classList.add('zoom-out-transition');
            
            // 同时开始启动界面的进入动画
            setTimeout(() => {
                if (startupScreen) {
                    startupScreen.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
                    startupScreen.style.opacity = '1';
                    startupScreen.style.transform = 'scale(1)';
                }
            }, 50);
            
            // 延迟隐藏隧道容器
            setTimeout(() => {
                tunnelContainer.style.display = 'none';
                tunnelContainer.classList.remove('zoom-out-transition');
                
                // 重置状态
                this.isStarted = false;
                this.currentIndex = 0;
                this.updatePhotoStack();
                
                // 清理启动界面的内联样式
                if (startupScreen) {
                    setTimeout(() => {
                        startupScreen.style.transition = '';
                        startupScreen.style.opacity = '';
                        startupScreen.style.transform = '';
                    }, 100);
                }
            }, 500);
        }
    }
    
    bindEvents() {
        // 键盘事件
        document.addEventListener('keydown', (e) => {
            if (!this.isStarted) return;
            
            switch(e.key) {
                case 'ArrowLeft':
                    e.preventDefault();
                    this.previousPhoto();
                    break;
                case 'ArrowRight':
                    e.preventDefault();
                    this.nextPhoto();
                    break;
                case 'Escape':
                    e.preventDefault();
                    this.backToStart();
                    break;
                case ' ':
                    e.preventDefault();
                    if (this.autoSlideInterval) {
                        this.stopAutoSlideshow();
                    } else {
                        this.startAutoSlideshow();
                    }
                    break;
            }
        });

        // 触摸事件支持
        let touchStartX = 0;
        let touchStartY = 0;
        let touchEndX = 0;
        let touchEndY = 0;
        let isSwiping = false;

        const photoStack = document.querySelector('.photo-stack');
        
        // 触摸开始
        photoStack.addEventListener('touchstart', (e) => {
            if (!this.isStarted) return;
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
            isSwiping = true;
        }, { passive: true });

        // 触摸移动
        photoStack.addEventListener('touchmove', (e) => {
            if (!this.isStarted || !isSwiping) return;
            e.preventDefault(); // 防止页面滚动
        }, { passive: false });

        // 触摸结束
        photoStack.addEventListener('touchend', (e) => {
            if (!this.isStarted || !isSwiping) return;
            
            touchEndX = e.changedTouches[0].clientX;
            touchEndY = e.changedTouches[0].clientY;
            
            const deltaX = touchEndX - touchStartX;
            const deltaY = touchEndY - touchStartY;
            const minSwipeDistance = 50;
            
            // 确保是水平滑动而不是垂直滑动
            if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > minSwipeDistance) {
                if (deltaX > 0) {
                    // 向右滑动，显示上一张
                    this.previousPhoto();
                } else {
                    // 向左滑动，显示下一张
                    this.nextPhoto();
                }
            }
            
            isSwiping = false;
        }, { passive: true });

        // 鼠标事件（桌面端）
        photoStack.addEventListener('click', (e) => {
            if (!this.isStarted) return;
            
            const rect = photoStack.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            const centerX = rect.width / 2;
            
            if (clickX < centerX) {
                this.previousPhoto();
            } else {
                this.nextPhoto();
            }
        });

        // 防止双击缩放
        document.addEventListener('touchstart', (e) => {
            if (e.touches.length > 1) {
                e.preventDefault();
            }
        }, { passive: false });

        let lastTouchEnd = 0;
        document.addEventListener('touchend', (e) => {
            const now = (new Date()).getTime();
            if (now - lastTouchEnd <= 300) {
                e.preventDefault();
            }
            lastTouchEnd = now;
        }, { passive: false });

        // 鼠标滚轮事件
        document.addEventListener('wheel', (e) => {
            if (!this.isStarted) return;
            
            e.preventDefault();
            
            if (e.deltaY > 0) {
                this.nextPhoto();
            } else {
                this.previousPhoto();
            }
        }, { passive: false });
    }

    // 绑定页面切换按钮事件
    bindPageSwitchEvents() {
        console.log('开始绑定页面切换事件...');
        
        const nextPageBtn = document.getElementById('nextPageBtn');
        const backToAlbumBtn = document.getElementById('backToAlbumBtn');
        
        console.log('下一页按钮:', nextPageBtn);
        console.log('返回相册按钮:', backToAlbumBtn);
        
        if (nextPageBtn) {
            nextPageBtn.addEventListener('click', (e) => {
                e.preventDefault();
                console.log('下一页按钮被点击');
                this.showLoveDeclaration();
            });
            console.log('下一页按钮事件已绑定');
        } else {
            console.error('未找到下一页按钮');
        }
        
        if (backToAlbumBtn) {
            backToAlbumBtn.addEventListener('click', (e) => {
                e.preventDefault();
                console.log('返回相册按钮被点击');
                this.hideLoveDeclaration();
            });
            console.log('返回相册按钮事件已绑定');
        } else {
            console.error('未找到返回相册按钮');
        }
    }
    

    
    createFloatingParticles() {
        // 持续的浮动粒子效果
        setInterval(() => {
            if (this.isStarted) {
                this.createFloatingParticle();
            }
        }, 2000);
    }

    createFloatingParticle() {
        const particles = ['✨', '💫', '⭐', '🌟'];
        const particle = document.createElement('div');
        particle.style.position = 'fixed';
        particle.style.pointerEvents = 'none';
        particle.style.zIndex = '5';
        particle.style.fontSize = '14px';
        particle.textContent = particles[Math.floor(Math.random() * particles.length)];
        
        const x = Math.random() * window.innerWidth;
        particle.style.left = x + 'px';
        particle.style.top = window.innerHeight + 'px';
        
        document.body.appendChild(particle);
        
        particle.animate([
            { 
                top: window.innerHeight + 'px',
                opacity: 0,
                transform: 'rotate(0deg)'
            },
            { 
                opacity: 0.8,
                offset: 0.1
            },
            { 
                top: '-50px',
                opacity: 0,
                transform: 'rotate(360deg)'
            }
        ], {
            duration: 8000,
            easing: 'linear'
        }).onfinish = () => {
            particle.remove();
        };
    }

    // 显示爱情宣言页面
    showLoveDeclaration() {
        console.log('显示爱情宣言页面');
        const loveDeclarationPage = document.querySelector('.love-declaration-page');
        const tunnelContainer = document.querySelector('.tunnel-container');
        
        console.log('爱情宣言页面元素:', loveDeclarationPage);
        console.log('隧道容器元素:', tunnelContainer);
        
        if (loveDeclarationPage && tunnelContainer) {
            // 添加远近拉伸镜头感切换动画到相册界面
            tunnelContainer.classList.add('zoom-out-transition');
            
            // 延迟隐藏相册界面
            setTimeout(() => {
                tunnelContainer.style.display = 'none';
                tunnelContainer.classList.remove('zoom-out-transition');
            }, 500);
            
            // 显示爱情宣言页面并添加远近拉伸镜头感切换动画
            // 稍微延迟显示，避免黑屏
            setTimeout(() => {
                loveDeclarationPage.classList.add('show');
                // 确保页面可见性
                loveDeclarationPage.style.opacity = '1';
                loveDeclarationPage.style.transform = 'scale(1)';
                loveDeclarationPage.classList.add('zoom-in-transition');
                
                // 动画完成后清理类名，但保持可见状态
                setTimeout(() => {
                    loveDeclarationPage.classList.remove('zoom-in-transition');
                    // 确保页面保持可见
                    loveDeclarationPage.style.opacity = '1';
                    loveDeclarationPage.style.transform = 'scale(1)';
                }, 500);
            }, 100);
        } else {
            console.error('未找到必要的页面元素');
        }
    }

    // 隐藏爱情宣言页面
    hideLoveDeclaration() {
        console.log('隐藏爱情宣言页面');
        const loveDeclarationPage = document.querySelector('.love-declaration-page');
        const tunnelContainer = document.querySelector('.tunnel-container');
        
        console.log('爱情宣言页面元素:', loveDeclarationPage);
        console.log('隧道容器元素:', tunnelContainer);
        
        if (loveDeclarationPage && tunnelContainer) {
            // 添加远近拉伸镜头感切换动画到爱情宣言界面
            loveDeclarationPage.classList.add('zoom-out-transition');
            
            // 延迟隐藏爱情宣言界面
            setTimeout(() => {
                loveDeclarationPage.classList.remove('show');
                loveDeclarationPage.classList.remove('zoom-out-transition');
            }, 500);
            
            // 显示相册界面并添加远近拉伸镜头感切换动画
            // 稍微延迟显示，避免黑屏
            setTimeout(() => {
                tunnelContainer.style.display = 'block';
                // 确保相册界面可见性
                tunnelContainer.style.opacity = '1';
                tunnelContainer.style.transform = 'scale(1)';
                tunnelContainer.classList.add('zoom-in-transition');
                
                // 动画完成后清理类名，但保持可见状态
                setTimeout(() => {
                    tunnelContainer.classList.remove('zoom-in-transition');
                    // 确保相册界面保持可见
                    tunnelContainer.style.opacity = '1';
                    tunnelContainer.style.transform = 'scale(1)';
                }, 500);
            }, 100);
        } else {
            console.error('未找到必要的页面元素');
        }
    }
}

// 添加震动动画
const style = document.createElement('style');
style.textContent = `
    @keyframes stackShake {
        0%, 100% { transform: translate(-50%, -50%) rotateX(0deg); }
        25% { transform: translate(-50%, -50%) rotateX(2deg); }
        75% { transform: translate(-50%, -50%) rotateX(-2deg); }
    }
`;
document.head.appendChild(style);

// 星空和烟花动画类
class StarryFireworks {
    constructor() {
        this.fireworksInterval = null;
        this.init();
    }

    init() {
        this.createStarryBackground();
        this.startFireworks();
    }

    createStarryBackground() {
        // 为启动界面添加星空
        const startupScreen = document.querySelector('.startup-screen');
        if (startupScreen) {
            this.addStarsToElement(startupScreen);
        }

        // 为爱情宣言页面添加星空
        const declarationPage = document.querySelector('.love-declaration-page');
        if (declarationPage) {
            this.addStarsToElement(declarationPage);
        }
    }

    addStarsToElement(element) {
        const starryContainer = document.createElement('div');
        starryContainer.className = 'starry-sky';
        
        // 创建100颗星星
        for (let i = 0; i < 100; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            
            // 随机大小
            const sizes = ['small', 'medium', 'large'];
            const randomSize = sizes[Math.floor(Math.random() * sizes.length)];
            star.classList.add(randomSize);
            
            // 随机位置
            star.style.left = Math.random() * 100 + '%';
            star.style.top = Math.random() * 100 + '%';
            
            // 随机动画延迟
            star.style.animationDelay = Math.random() * 2 + 's';
            
            starryContainer.appendChild(star);
        }
        
        element.appendChild(starryContainer);
    }

    startFireworks() {
        this.fireworksInterval = setInterval(() => {
            this.createFirework();
        }, 1200); // 每1.2秒创建一个烟花
    }

    createFirework() {
        const containers = [
            document.querySelector('.startup-screen'),
            document.querySelector('.love-declaration-page')
        ];
        
        containers.forEach(container => {
            if (container && (container.style.display !== 'none' || container.classList.contains('fade-in'))) {
                // 随机生成1-3个烟花
                const fireworkCount = Math.floor(Math.random() * 3) + 1;
                for (let i = 0; i < fireworkCount; i++) {
                    setTimeout(() => {
                        this.launchFirework(container);
                    }, i * 300); // 每个烟花间隔300ms
                }
            }
        });
    }

    launchFirework(container) {
        // 随机发射位置（底部）
        const startX = Math.random() * container.offsetWidth;
        const startY = container.offsetHeight;
        
        // 随机爆炸位置（上半部分）
        const endX = Math.random() * container.offsetWidth;
        const endY = Math.random() * container.offsetHeight * 0.4 + container.offsetHeight * 0.1;
        
        // 创建烟花轨迹
        const trail = document.createElement('div');
        trail.className = 'firework-trail';
        trail.style.left = startX + 'px';
        trail.style.top = startY + 'px';
        trail.style.background = `linear-gradient(to top, 
            rgba(255, 255, 255, 0.8) 0%, 
            rgba(255, 215, 0, 0.6) 30%, 
            rgba(255, 165, 0, 0.4) 60%, 
            transparent 100%)`;
        trail.style.width = '3px';
        trail.style.borderRadius = '2px';
        trail.style.transformOrigin = 'bottom center';
        
        // 计算轨迹角度和长度
        const deltaX = endX - startX;
        const deltaY = endY - startY;
        const distance = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
        const angle = Math.atan2(deltaX, -deltaY) * (180 / Math.PI);
        
        trail.style.height = distance + 'px';
        trail.style.transform = `rotate(${angle}deg)`;
        
        container.appendChild(trail);
        
        // 延迟创建爆炸效果
        setTimeout(() => {
            const firework = document.createElement('div');
            firework.className = 'firework';
            firework.style.left = endX + 'px';
            firework.style.top = endY + 'px';
            
            this.createExplosion(firework, endX, endY);
            container.appendChild(firework);
            
            // 清理烟花
            setTimeout(() => {
                if (firework.parentNode) {
                    firework.parentNode.removeChild(firework);
                }
            }, 1500);
        }, 1000);
        
        // 清理轨迹
        setTimeout(() => {
            if (trail.parentNode) {
                trail.parentNode.removeChild(trail);
            }
        }, 1200);
    }

    createExplosion(firework, x, y) {
        const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#ffd93d', '#ff9ff3', '#a8e6cf', '#ff8a80', '#82b1ff', '#b388ff', '#ffab40'];
        const particleCount = 16;
        
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'firework-particle';
            
            const angle = (i / particleCount) * Math.PI * 2;
            const distance = 50 + Math.random() * 50;
            const dx = Math.cos(angle) * distance;
            const dy = Math.sin(angle) * distance;
            
            particle.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            particle.style.setProperty('--dx', dx + 'px');
            particle.style.setProperty('--dy', dy + 'px');
            
            firework.appendChild(particle);
        }
    }

    destroy() {
        if (this.fireworksInterval) {
            clearInterval(this.fireworksInterval);
        }
    }
}

// 初始化相册
document.addEventListener('DOMContentLoaded', () => {
    // 初始化音频播放器
    const musicPlayer = new MusicPlayer();
    
    // 初始化星空烟花效果
    const starryFireworks = new StarryFireworks();
    
    const album = new TunnelPhotoAlbum();
    
    // 绑定页面切换按钮事件（确保DOM已加载）
    album.bindPageSwitchEvents();
    
    // 显示欢迎消息
    console.log('🎉 时空隧道照片相册已加载！');
    console.log('💡 操作提示：');
    console.log('   - 点击"开始旅程"按钮启动相册');
    console.log('   - 使用左右箭头键或点击按钮切换照片');
    console.log('   - 按空格键暂停/继续自动播放');
    console.log('   - 按ESC键返回启动界面');
    console.log('   - 支持触摸滑动和鼠标滚轮操作');
});