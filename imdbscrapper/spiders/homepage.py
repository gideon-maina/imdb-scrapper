import logging

import scrapy


class HomepageSpider(scrapy.Spider):
    name = 'homepage'
    allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/']

    def parse(self, response):
        yield from self.parse_trailers(response)
        yield from self.parse_featured_today(response)

    def parse_trailers(self, response):
        # Get the current trailers showing
        trailers = response.css('div.swiper-slide')
        for trailer in trailers:
            title = trailer.css(
                'div.SlideCaptionstyles__CaptionHeading-sc-8h388a-2'
            ).css(
                'span.SlideCaptionstyles__CaptionHeadingText-sc-8h388a-4.dGEdPt::text'
            ).get()
            image_link = trailer.css(
                'div.AutorotateWithPeekSlidestyles__WithPeekDesktopTitlePoster-sc-85l9zx-4'
            ).css('div.ipc-media').css('img::attr(src)').get()
            video = trailer.css(
                'div.VideoSlateWithPeekstyles__WithPeekSlateContainer-oyjpyw-0'
            ).css('a.ipc-lockup-overlay.ipc-focusable::attr(href)').get()
            movie_info_link = trailer.css(
                'div.AutorotateWithPeekSlidestyles__WithPeekDesktopTitlePoster-sc-85l9zx-4'
            ).css('a.ipc-lockup-overlay.ipc-focusable::attr(href)').get()
            duration_trailer = trailer.css(
                'div.SlideCaptionstyles__CaptionHeading-sc-8h388a-2'
            ).css(
                'span.SlideCaptionstyles__DesktopRuntimeText-sc-8h388a-8.guCVCB::text'
            ).get()
            tr = {}
            tr['title'] = title
            tr['image_link'] = image_link
            tr['video'] = video
            tr['movie_info_link'] = movie_info_link
            tr['duration_trailer'] = duration_trailer
            yield tr

    def parse_featured_today(self, response):
        # Get thea featured today
        featured_today = response.css('section.ipc-page-section.featured-today'
                                      ).css('div.TmuaKOoDo-QlBHQGmOX1k')

        for feature in featured_today:
            title = feature.css('a.Rwa4i3rwtfq5LpCcukrtG::text').get()
            image_link = feature.css('div.ipc-media').css(
                'img::attr(src)').get()
            video_link = feature.css(
                'a.Rwa4i3rwtfq5LpCcukrtG::attr(href)').get()
            fr = {}
            fr['title'] = title
            fr['image_link'] = image_link
            fr['video_link'] = video_link

            yield fr

        # Get the What to watch

        # Get Watch free on IMDB

        # Get Explore what's streaming

        # Get Explore Movies and TV Shows

        # Get More to explore
