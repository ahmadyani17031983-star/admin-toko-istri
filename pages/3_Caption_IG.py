import streamlit as st
import random

st.header("3. Pembuat Caption & Tagar Instagram - Oskaria")

kategori = st.selectbox("Kategori Produk", [
    "Parcel Buah & Buah Hias",
    "Puding Segar",
    "Buah Segar Impor",
    "Kue Basah (PO)",
    "Kue Kering & Hampers"
])

menu = st.text_input("Nama Menu / Varian", "Parcel Buah Mix Apel & Anggur")
keunggulan = st.text_input("Keunggulan / Promo", "Buah fresh pilihan, bisa custom isi & gratis kartu ucapan")
kota = st.text_input("Area Kirim", "Sidrap & Wajo")
wa = st.text_input("Nomor WhatsApp", "0851-7545-8884")
gaya = st.radio("Gaya Bahasa", ["Ramah & Hangat", "Singkat & Promo"], horizontal=True)

if st.button("Buat Caption Sekarang", type="primary"):
    pembuka = {
        "Parcel Buah & Buah Hias": [
            f"Mau jenguk kerabat atau kirim bingkisan spesial di area {kota}? 🎁🍎",
            f"Sampaikan perhatian manis lewat rangkaian {menu} dari Oskaria yang rapi dan segar ✨"
        ],
        "Puding Segar": [
            f"Cuaca panas paling pas ditemani yang lembut dan dingin! 🍮✨",
            f"Cari dessert lembut untuk keluarga di {kota}? Cobain {menu} buatan Oskaria! 😋"
        ],
        "Buah Segar Impor": [
            f"Baru datang di Oskaria! Stok {menu} manis dan renyah siap masuk kulkas di rumah 🍇🍊",
            f"Jaga kesehatan keluarga dengan pilihan {menu} kualitas terbaik hari ini 🍎✨"
        ],
        "Kue Basah (PO)": [
            f"Butuh suguhan untuk arisan, pengajian, atau rapat di {kota}? 🥮☕",
            f"Fresh dari dapur Oskaria! Open PO {menu} buatan rumahan tanpa pengawet 🌿"
        ],
        "Kue Kering & Hampers": [
            f"Teman ngeteh sore paling pas atau ide hampers cantik dari Oskaria untuk orang tersayang 🍪🎁",
            f"Renyah dan wangi butter! {menu} siap menemani momen kumpul keluarga ✨"
        ]
    }

    tagar = {
        "Parcel Buah & Buah Hias": "#parcelbuahsidrap #parcelbuahwajo #buahhiassidrap #buahhiaswajo #hampersbuahsidrap #hampersbuahwajo #parceljenguk",
        "Puding Segar": "#pudingsidrap #pudingwajo #dessertsidrap #dessertwajo #pudinghomemade #kulinersidrap #kulinerwajo",
        "Buah Segar Impor": "#buahsegarsidrap #buahsegarwajo #buahimporsidrap #buahimporwajo #tokobuahsidrap #tokobuahwajo",
        "Kue Basah (PO)": "#kuebasahsidrap #kuebasahwajo #snackboxsidrap #snackboxwajo #kuearisan #kulinersidrap #kulinerwajo",
        "Kue Kering & Hampers": "#kuekeringsidrap #kuekeringwajo #hamperskuesidrap #hamperskuewajo #topleskue #kulinersidrap #kulinerwajo"
    }

    awal = random.choice(pembuka[kategori])

    if gaya == "Ramah & Hangat":
        teks = (
            f"{awal}\n\n"
            f"✨ *{menu}* — by Oskaria\n"
            f"✅ {keunggulan}\n"
            f"🚚 Siap antar area {kota}\n\n"
            f"Yuk amankan pesananmu sekarang sebelum kehabisan! 😊\n"
            f"📲 Order via WhatsApp: {wa}\n"
            f"📸 Instagram: @Oskaria.19\n\n"
            f".\n.\n"
            f"{tagar[kategori]} #oskaria #umkmsidrap #umkmwajo"
        )
    else:
        teks = (
            f"READY / OPEN PO DI OSKARIA: {menu.upper()}! 🔥\n\n"
            f"• {keunggulan}\n"
            f"• Pengiriman area {kota}\n\n"
            f"Pesan cepat via WA: {wa} 📲 | IG: @Oskaria.19\n\n"
            f"{tagar[kategori]} #oskaria"
        )

    st.subheader("Hasil Caption Siap Salin:")
    st.code(teks, language=None)
