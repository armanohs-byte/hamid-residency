# Hamid Residency — Official Property Portal
**Khagrabari, Cooch Behar, West Bengal, India**

A fast, mobile-optimized, high-conversion residential rental web application built for **Hamid Residency**.

---

## 🌟 Key Features Built

1. **Brand & Visual Identity**:
   - Custom architectural vector badge logo (`assets/images/logo.svg`).
   - Deep forest green (`#0f3b2e`), warm gold (`#c2913e`), and crisp tile white color scheme reflecting residential serenity and modern cleanliness.
   - High-performance, zero-framework architecture (pure modern semantic HTML5, CSS3, ES6 JavaScript) with sub-second load times.

2. **Accurate, Truthful Property Narrative**:
   - Highlights the verified property facts: 3-storey standalone building, modular kitchen with black chimney, extensive white tile work, modern tiled bathrooms, white-framed glass windows, and standout 1st floor features.
   - Explicit **Transparency Notice** clearly informing tenants that representative architectural visuals are currently showcased while high-resolution photography is updated, welcoming them for an in-person viewing.
   - Refrains from inventing unverified specifications (exact rent, dimensions, room count).

3. **Floor-by-Floor Interactive Breakdown**:
   - **Ground Floor**: Zero-stair level access, ideal for seniors and families with children.
   - **First Floor (Flagship Suite)**: Standout floor with modular kitchen, black chimney, and premium tiles.
   - **Second Floor**: Elevated tranquility, cross-ventilation, and green neighborhood views.
   - Clicking any floor card automatically pre-selects that unit in the rental enquiry form.

4. **Strategic Locality & Transit Intelligence**:
   - **New Cooch Behar Junction (NCB)**: ~3.5 km (8–12 mins commute via Toto/car). Direct Shatabdi, Rajdhani, Padatik, Vande Bharat connectivity.
   - **National Highway 31 (NH-31)**: Immediate access (< 1 km) towards Siliguri and Assam.
   - **Healthcare**: MJN Medical College & Hospital (~4 km).
   - **Culture**: Cooch Behar Royal Palace, Madan Mohan Bari, Sagardighi Lake (~4.5 km).

5. **High-Conversion Contact & Visit Flow**:
   - **Instant WhatsApp Pre-filled Chat Engine**: Formulates a complete, structured message with tenant type, preferred floor, move-in timeframe, and visit request.
   - **One-Tap Phone Call CTA**: Easy calling for direct landlord conversations with zero brokerage fees.
   - **Persistent Mobile Action Bar**: Floating sticky contact bar on smartphones for instantaneous tap-to-call and WhatsApp engagement.
   - **Interactive Image Lightbox**: High-resolution image viewer with caption labels.

6. **SEO & Discoverability**:
   - OpenGraph meta tags for WhatsApp/Facebook link previews.
   - Schema.org JSON-LD `ApartmentComplex` structured data with Khagrabari geolocation coordinates (26.342763, 89.4452924).
   - Search engine `robots.txt` and `sitemap.xml`.

---

## 🚀 How to Run the Website Locally

You can run the website immediately using Python:

```bash
cd hamid-residency
python server.py
```

Then open your browser to:
**http://localhost:8080**

*(You can also simply double-click `index.html` to open it directly in any browser!)*

---

## 📸 Replacing Representative Images with Real Photographs

The website is designed so you can replace the AI representative images with real photos without touching any code!

Simply save your real photos with these exact file names in `hamid-residency/assets/images/`:

| File Name | Description |
|-----------|-------------|
| `exterior-facade.jpg` | Building exterior view from the road/gate |
| `modular-kitchen.jpg` | Kitchen showing white tile work & black chimney |
| `modern-bathroom.jpg` | Contemporary tiled bathroom & fittings |
| `first-floor-living.jpg` | First-floor living room or main hall |
| `bright-bedroom.jpg` | Bedroom showing white-framed windows & natural light |

Once you drop in the real photos, you can remove or hide the `<aside class="transparency-banner">` in `index.html`.

---

## 📞 How to Update Your Phone & WhatsApp Number

To connect your real mobile number, update the configuration in:

1. **`assets/js/enquiry.js`** (Line 7):
   ```javascript
   const OWNER_CONFIG = {
     phoneDisplay: "+91 YOUR_NUMBER_HERE",
     phoneRaw: "91YOURNUMBERHERE", // No spaces, include country code (e.g. 918420838820)
     propertyName: "Hamid Residency, Khagrabari, Cooch Behar"
   };
   ```
2. **`assets/data/property-data.json`**:
   Update `phoneDisplay`, `phoneRaw`, and `whatsappNumber`.

---

## 🌐 Instant Free Hosting Options

The entire site has **zero build steps** and runs as a pure static web app. You can deploy it for free:

- **Netlify**: Drag and drop the `hamid-residency` folder into [app.netlify.com/drop](https://app.netlify.com/drop).
- **GitHub Pages**: Push this folder to a GitHub repository and enable Pages in repository settings.
- **Vercel / Cloudflare Pages / Shared Host**: Upload the folder files directly to the `public_html` root.
