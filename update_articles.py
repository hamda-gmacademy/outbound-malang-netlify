import re

files = ["c:/Users/aisya/Downloads/GM Academy/outbound-malang-2/article1.html",
         "c:/Users/aisya/Downloads/GM Academy/outbound-malang-2/article2.html",
         "c:/Users/aisya/Downloads/GM Academy/outbound-malang-2/article3.html"]

def modify_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add Open Sans font
    if "family=Open+Sans" not in content:
        content = content.replace('rel="stylesheet" />\n    <style>', 'rel="stylesheet" />\n    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet" />\n    <style>')

    # 2. Update CSS
    css_old = """        .article-content {
            font-family: 'Noto Sans', sans-serif;
            font-size: 1.125rem;
            line-height: 1.8;
            color: #4b5563;
        }

        .article-content h2 {
            font-size: 1.75rem;
            font-weight: 700;
            color: var(--text-main);
            margin-top: 48px;
            margin-bottom: 16px;
            font-family: 'Be Vietnam Pro', sans-serif;
        }

        .article-content p {
            margin-bottom: 24px;
        }

        .article-content ul {
            margin-bottom: 24px;
            padding-left: 24px;
        }

        .article-content li {
            margin-bottom: 8px;
        }"""
    
    css_new = """        /* Modified standard word style */
        .article-content {
            font-family: 'Open Sans', sans-serif;
            font-size: 16px; /* 12 pt */
            line-height: 1; /* single spacing */
            color: #4b5563;
        }
        .article-content h1, .article-content h2, .article-content h3, .article-content h4 {
            font-family: 'Be Vietnam Pro', sans-serif;
        }
        .article-content h2 {
            font-size: 1.75rem;
            font-weight: 700;
            color: var(--text-main);
            margin-top: 48px;
            margin-bottom: 16px;
        }
        .article-content p {
            margin-top: 0;
            margin-bottom: 8pt; /* Word spacing after 8pt */
        }
        .article-content ul {
            margin-bottom: 8pt;
            padding-left: 24px;
        }
        .article-content li {
            margin-bottom: 8px;
        }
        .image-caption { font-size: 14px; text-align: center; color: var(--text-light); margin-top: -24px; margin-bottom: 40px; font-style: italic; }
        .toc-container { background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 8px; padding: 16px; margin-bottom: 24px; }
        .toc-container summary { font-weight: bold; cursor: pointer; font-size: 18px; color: var(--primary); }
        .toc-container ul { margin-top: 12px; list-style: none; padding-left: 0; }
        .toc-container ul li { margin-bottom: 8px; }
        .toc-container a { color: var(--text-main); text-decoration: none; }
        .toc-container a:hover { color: var(--primary); text-decoration: underline; }
        .baca-juga { background-color: #e3f2fd; border-left: 4px solid var(--primary); padding: 16px; margin: 24px 0; border-radius: 0 8px 8px 0; }
        .baca-juga h4 { margin-top: 0; margin-bottom: 12px; color: var(--primary-dark); font-size: 18px; }
        blockquote { border-left: 4px solid var(--secondary); background: #f1f8f5; padding: 16px 20px; margin: 24px 0; font-style: italic; color: #2d6a4f; border-radius: 0 8px 8px 0; }
        .promo-gif { display: block; max-width: 100%; margin: 32px auto; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .supporting-figure { margin: 32px 0; text-align: center; }
        .supporting-figure img { max-width: 100%; border-radius: 12px; }
        .supporting-figure figcaption { font-size: 14px; color: #6c757d; margin-top: 8px; font-style: italic; }
        .faq-item { margin-bottom: 16px; border-bottom: 1px solid #e5e7eb; padding-bottom: 16px; }
        .faq-item summary { font-weight: bold; cursor: pointer; color: var(--text-main); font-size: 18px; }
        .faq-item p { margin-top: 12px; color: #4b5563; line-height: 1.5; }
        .author-profile { display: flex; align-items: center; gap: 16px; margin-top: 48px; padding-top: 24px; border-top: 1px solid #e5e7eb; }
        .author-profile img { width: 64px; height: 64px; border-radius: 50%; object-fit: cover; }
        .author-info h4 { margin-bottom: 4px; font-size: 18px; color: #000; }
        .author-info p { margin: 0; font-size: 14px; color: var(--text-light); }
        .share-buttons { display: flex; gap: 12px; margin-top: 24px; }
        .share-btn { display: inline-flex; align-items: center; gap: 8px; padding: 8px 16px; border-radius: 20px; text-decoration: none; font-size: 14px; font-weight: 600; color: white; transition: opacity 0.2s; }
        .share-btn:hover { opacity: 0.9; }
        .share-wa { background-color: #25D366; }
        .share-fb { background-color: #1877F2; }
        .share-tw { background-color: #000000; }
        .related-articles-section { margin-top: 64px; border-top: 1px solid #e5e7eb; padding-top: 48px; margin-bottom: 48px;}
        .related-articles-section > h3 { font-size: 24px; margin-bottom: 24px; color: var(--text-main); }
        .related-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px; }
        .related-card { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05); display: flex; flex-direction: column; }
        .related-card img { width: 100%; height: 160px; object-fit: cover; }
        .related-card-content { padding: 16px; display: flex; flex-direction: column; flex: 1; }
        .related-card h4 { font-size: 16px; margin-bottom: 8px; line-height: 1.4; color: #000; }
        .related-card p { font-size: 14px; color: var(--text-light); margin-bottom: 16px; flex: 1; line-height: 1.4; }
        .related-btn { display: inline-block; padding: 8px; background-color: var(--primary); color: white; text-decoration: none; border-radius: 6px; font-size: 14px; font-weight: bold; text-align: center; transition: background 0.2s; }
        .related-btn:hover { background-color: var(--primary-dark); }"""
    
    content = content.replace(css_old, css_new)

    # 3. Add Image Caption
    if "Deskripsi: Para pendaki" not in content:
        content = re.sub(r'(<img class="article-hero-img" [^>]*>)',
                         r'\1\n            <p class="image-caption">Deskripsi: Para pendaki sedang menyusuri keindahan alam bebas di Malang, menikmati udara segar dan kebersamaan.</p>',
                         content)

    # 4. Insert TOC
    if "toc-container" not in content:
        content = content.replace('<div class="article-content">',
                                  '<div class="article-content">\n                <div class="toc-container">\n                    <details open>\n                        <summary>Daftar Isi</summary>\n                        <ul id="toc-list"></ul>\n                    </details>\n                </div>')

    # 5. Baca Juga
    if "baca-juga" not in content:
        find_text = "Mari kita selami lebih dalam!</p>"
        replace_text = """Mari kita selami lebih dalam!</p>

                <div class="baca-juga">
                    <h4>Baca Juga:</h4>
                    <ul>
                        <li><a href="article2.html">Mengapa Bonding di Luar Ruangan Lebih Baik untuk Moral</a></li>
                        <li><a href="article3.html">Utamakan Keselamatan: Panduan Kami untuk Petualangan yang Aman</a></li>
                    </ul>
                </div>"""
        content = content.replace(find_text, replace_text)

    # 6. Blockquote
    if "blockquote" not in content:
        find_text2 = "<h2>1. Jalur Bukit Nirwana (Pujon)</h2>"
        replace_text2 = """<blockquote>"Petualangan terbaik bukanlah tentang menaklukkan alam, tapi menaklukkan diri sendiri dan menyatu dengan tim." <br>- Tim Spesialis Outbound</blockquote>

                <h2>1. Jalur Bukit Nirwana (Pujon)</h2>"""
        content = content.replace(find_text2, replace_text2)

    # 7. Promo Gif and Supporting Image
    if "promo-gif" not in content:
        find_text3 = "<h2>4. Hutan Pinus Jalur Lintas Paralayang</h2>"
        replace_text3 = """<img src="https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif" alt="Promo Outbound" class="promo-gif" />

                <figure class="supporting-figure">
                    <img src="https://images.unsplash.com/photo-1551632811-561732d1e306?auto=format&fit=crop&q=80&w=800" alt="Tim Outbound sedang bermain games">
                    <figcaption>Gambar pendukung: Peserta outbound menikmati permainan membangun kekompakan.</figcaption>
                </figure>

                <h2>4. Hutan Pinus Jalur Lintas Paralayang</h2>"""
        content = content.replace(find_text3, replace_text3)

    # 8. Kesimpulan & FAQ & Author & Related (The End of Content)
    if "<h2>Kesimpulan</h2>" not in content:
        find_text4 = "standar keselamatan tertinggi.</p>\n            </div>\n        </div>"
        replace_text4 = """standar keselamatan tertinggi.</p>
                
                <h2>Kesimpulan</h2>
                <p>Mengeksplorasi alam melalui aktivitas rekreasi dan outbound memberikan jembatan pengalaman yang luar biasa. Tidak hanya menyehatkan fisik, namun juga membangun sinergi dan kolaborasi antar individu secara efektif. Persiapan yang matang serta bantuan pendampingan profesional sangat direkomendasikan agar setiap perjalanan memberikan makna dan ingatan mendalam.</p>

                <h2>FAQ (Pertanyaan yang Sering Diajukan)</h2>
                <div class="faq-item">
                    <details>
                        <summary>Apakah program ini aman untuk orang yang jarang olahraga?</summary>
                        <p>Tentu saja. Kami selalu menyesuaikan intensitas program dan rute perjalanan berdasarkan kondisi fisik peserta, didukung oleh tim profesional dengan alat pelindung standar.</p>
                    </details>
                </div>
                <div class="faq-item">
                    <details>
                        <summary>Bagaimana cara melakukan reservasi?</summary>
                        <p>Anda bisa menekan tombol WhatsApp yang melayang pada layar Anda, atau mengirimkan email melalui form pada halaman kontak kami untuk menanyakan penawaran harga menarik.</p>
                    </details>
                </div>

                <img src="https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif" alt="Terima Kasih Gif" class="promo-gif" />
            </div>

            <div class="author-profile">
                <img src="https://ui-avatars.com/api/?name=Tim+Editor&background=0077b8&color=fff" alt="Profil Penulis">
                <div class="author-info">
                    <h4>Tim Publikasi</h4>
                    <p>Penulis spesialis outdoor activity dan team building korporat.</p>
                </div>
            </div>

            <div class="share-buttons">
                <a href="https://wa.me/?text=Halo,%20saya%20membaca%20artikel%20ini!" target="_blank" class="share-btn share-wa">
                    <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c-.003 1.396.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326z"/></svg>
                    <span>Bagikan ke WA</span>
                </a>
                <a href="https://facebook.com/sharer/sharer.php?u=#" target="_blank" class="share-btn share-fb">
                    <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/></svg>
                    <span>Share ke FB</span>
                </a>
                <a href="https://twitter.com/intent/tweet?text=Cek%20artikel%20ini!&url=#" target="_blank" class="share-btn share-tw">
                    <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M12.6.75h2.454l-5.36 6.142L16 15.25h-4.937l-3.867-5.07-4.425 5.07H.316l5.733-6.57L0 .75h5.063l3.495 4.633L12.601.75Zm-.86 13.028h1.36L4.323 2.145H2.865l8.875 11.633Z"/></svg>
                    <span>Tweet ini</span>
                </a>
            </div>

            <div class="related-articles-section">
                <h3>Artikel Terkait</h3>
                <div class="related-grid">
                    <div class="related-card">
                        <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=400" alt="Artikel Pertama">
                        <div class="related-card-content">
                            <h4>Manfaat Team Building di Alam</h4>
                            <p>Ketahui bagaimana aktivitas alam dapat meningkatkan kolaborasi tim Anda.</p>
                            <a href="article2.html" class="related-btn">Baca Selengkapnya</a>
                        </div>
                    </div>
                    <div class="related-card">
                        <img src="https://images.unsplash.com/photo-1537210249814-b9a10a161ae4?auto=format&fit=crop&q=80&w=400" alt="Artikel Kedua">
                        <div class="related-card-content">
                            <h4>Persiapan Sebelum Ke Malang</h4>
                            <p>Tips persiapan fisik, logistik, mental sebelum petualangan di Malang.</p>
                            <a href="article3.html" class="related-btn">Baca Selengkapnya</a>
                        </div>
                    </div>
                    <div class="related-card">
                        <img src="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&q=80&w=400" alt="Artikel Ketiga">
                        <div class="related-card-content">
                            <h4>Fun Games Favorit Perusahaan</h4>
                            <p>Daftar permainan seru yang sering diminta dan berdampak positif.</p>
                            <a href="article1.html" class="related-btn">Baca Selengkapnya</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""
        content = content.replace(find_text4, replace_text4)

    # 9. Inject JS
    if "id = id;" not in content:
        find_script = "function closeMobileMenu() {\n            mobileMenu.classList.remove('open');\n        }"
        replace_script = """function closeMobileMenu() {
            mobileMenu.classList.remove('open');
        }

        document.addEventListener("DOMContentLoaded", function () {
            const content = document.querySelector(".article-content");
            if(content) {
                const headings = content.querySelectorAll("h2, h3");
                const tocList = document.getElementById("toc-list");
                
                if (headings.length > 0 && tocList) {
                    headings.forEach((heading, index) => {
                        const id = "heading-" + index;
                        heading.id = id;
                        const li = document.createElement("li");
                        li.style.marginLeft = heading.tagName === "H3" ? "20px" : "0";
                        const a = document.createElement("a");
                        a.href = "#" + id;
                        a.textContent = heading.textContent;
                        li.appendChild(a);
                        tocList.appendChild(li);
                    });
                }
            }
        });"""
        content = content.replace(find_script, replace_script)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        print(f"Updated {filepath}")

for f in files:
    modify_file(f)
