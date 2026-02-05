// @ts-check
// Docusaurus configuration for Project Documentation documentation

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Asset Management',
  tagline: 'User Documentation',
  favicon: 'img/favicon.ico',

  url: 'https://docs.example.com',
  baseUrl: '/redacted-project/',

  organizationName: 'your-org',
  projectName: 'redacted-project-docs',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'es', 'fr'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: '/',
          editUrl: 'https://github.com/your-org/redacted-project-docs/edit/main/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Project Documentation',
        logo: {
          alt: 'Project Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'getting-started/index',
            position: 'left',
            label: 'Getting Started',
          },
          {
            type: 'doc',
            docId: 'roles/index',
            position: 'left',
            label: 'Roles',
          },
          {
            type: 'doc',
            docId: 'views/index',
            position: 'left',
            label: 'Views',
          },
          {
            type: 'localeDropdown',
            position: 'right',
          },
          {
            type: 'docsVersionDropdown',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Documentation',
            items: [
              { label: 'Getting Started', to: '/getting-started' },
              { label: 'User Roles', to: '/roles' },
              { label: 'Installation', to: '/installation' },
            ],
          },
          {
            title: 'Support',
            items: [
              { label: 'HelpDesk', href: 'mailto:helpdesk@example.com' },
              { label: 'IT Support', to: '/admin' },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Your Company. Documentation built with Docusaurus.`,
      },
      prism: {
        theme: require('prism-react-renderer').themes.github,
        darkTheme: require('prism-react-renderer').themes.dracula,
      },
      algolia: {
        // Optional: Configure Algolia DocSearch
        appId: 'YOUR_APP_ID',
        apiKey: 'YOUR_API_KEY',
        indexName: 'redacted-project',
      },
    }),
};

module.exports = config;
